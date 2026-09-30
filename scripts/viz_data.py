"""Build the page's data.json from rutas_changes.csv (new schema only, Dec 2024 onward).

Usage: viz_data.py <rutas_changes.csv> <data.json>

A section's state holds from one change to the next, so everything is measured in time:
hours per day in each estado, and the peak number of sections affected at the same moment.

- Episodes: maximal runs of non-open state for one section. Segments whose text names no cause
  borrow the episode's dominant known cause.
- Permanent listings: sections non-open for more than PERMANENT_SHARE of the period (e.g. RN 153
  "únicamente por RN 149") are listed separately and left out of every chart.
- Conflicts: status and text disagree, either a CORTE TOTAL whose text only describes a restriction,
  or a non-open status whose text says the road is passable. They are flagged, not reclassified.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

CHANGES, OUT = Path(sys.argv[1]), Path(sys.argv[2])
SEV = {"HABILITADA": 0, "RESTRINGIDA": 1, "CORTE PARCIAL": 2, "CORTE TOTAL": 3}
PERMANENT_SHARE = 0.95
MIN_EPISODE_H = 2  # shorter episodes are left out of the duration chart (mostly quick corrections)
CAUSES = [  # first match wins; order matters (e.g. "viento blanco" is snow)
    ("Nieve y hielo", r"niev|nevad|hielo|viento blanco|escarcha|cadenas|congel"),
    ("Viento", r"viento|r[aá]faga"),
    ("Lluvia y agua", r"lluvi|agua|inund|anega|crecid|barro|temporal|desborde|río|rio "),
    ("Derrumbe o aluvión", r"derrumb|aluvi|desliz|alud|piedra|roca|socav|hundim|colapso"),
    ("Obras", r"obra|trabaj|repavim|bacheo|puente|mantenimiento|carril|alternad"),
    ("Niebla", r"niebla|neblina|bruma"),
    ("Horario", r"horario|solo de \d|de \d+ a \d+ ?hs|cruce|paso internacional|aduana"),
    ("Otras", r"incend|humo|fuego|manifest|protest|piquete|gremi|movilizaci|animal|trashuman|accidente"),
]
CAUSE_RX = [(n, re.compile(p, re.I)) for n, p in CAUSES]
UNKNOWN = "Sin detalle"
NAMES = [c for c, _ in CAUSES] + [UNKNOWN]
RESTRICT = re.compile(r"restring", re.I)
CLOSED = re.compile(r"corte|cortad|cerrad|intransit|no transit|interrump|sin paso", re.I)
PASSABLE = re.compile(r"^\W*(transitable|tr[aá]nsito (normal|con precauc)|habilitad)", re.I)
PASSES = [  # full-closure durations for the border passes
    ("Mendoza", "7", "Tunel Internacional", "RN 7 · Cristo Redentor"),
    ("Neuquén", "242", "Aduana - Lte. con Chile", "RN 242 · Pino Hachado"),
    ("Mendoza", "145", "Paso Internacional El Pehuenche", "RN 145 · Pehuenche"),
    ("San Juan", "150", "Arrequintin - Lte. Con Chile", "RN 150 · Agua Negra"),
]


def cause(text):
    for name, rx in CAUSE_RX:
        if rx.search(text):
            return name
    return UNKNOWN


def conflict(estado, text):
    if estado == "CORTE TOTAL" and RESTRICT.search(text) and not CLOSED.search(text):
        return True
    # "Transitable" alone under a non-open status, or any passable text under a full closure
    bare = len(text) <= 30
    return bool(PASSABLE.search(text)) and not CLOSED.search(text) and (bare and SEV.get(estado, 0) > 0 or estado == "CORTE TOTAL")


def main():
    events = defaultdict(list)
    end = None
    for r in csv.DictReader(open(CHANGES)):
        if r["schema"] != "new":
            continue
        ts = datetime.fromisoformat(r["ts"].replace("Z", "+00:00"))
        end = max(end or ts, ts)
        est = None if r["event"] == "removed" else r["estado"]
        events[(r["region"], r["ruta"], r["tramo"])].append((ts, est, r["observaciones"]))

    day0 = min(e[0][0] for e in events.values()).replace(hour=0, minute=0, second=0, microsecond=0)
    ndays = (end - day0).days + 1
    period_h = (end - day0).total_seconds() / 3600

    # episodes: list of segments (start, end, sev, estado, text) per section
    episodes = defaultdict(list)
    for key, evs in events.items():
        cur = None
        for i, (ts, est, obs) in enumerate(evs):
            nxt = evs[i + 1][0] if i + 1 < len(evs) else end
            s = SEV.get(est, 0) if est else 0
            if s > 0 and nxt > ts:
                if cur is None:
                    cur = []
                    episodes[key].append(cur)
                cur.append((ts, nxt, s, est, obs))
            elif s == 0:
                cur = None

    # assign causes (borrowing within the episode) and conflict flags
    segs = defaultdict(list)  # key -> (a, b, sev, cause, conflict)
    for key, eps in episodes.items():
        for ep in eps:
            known = Counter()
            for a, b, s, est, obs in ep:
                c = cause(obs)
                if c != UNKNOWN:
                    known[c] += (b - a).total_seconds()
            fallback = known.most_common(1)[0][0] if known else UNKNOWN
            for a, b, s, est, obs in ep:
                c = cause(obs)
                segs[key].append((a, b, s, fallback if c == UNKNOWN else c, conflict(est, obs)))

    H = lambda a, b: (b - a).total_seconds() / 3600
    permanent = []
    for key in list(segs):
        bad = sum(H(a, b) for a, b, *_ in segs[key])
        if bad / period_h > PERMANENT_SHARE:
            obs = next((o for t, e, o in reversed(events[key]) if o), "")
            permanent.append({"region": key[0], "ruta": key[1], "tramo": key[2],
                              "estado": events[key][-1][1], "obs": obs, "share": round(bad / period_h, 3)})
            del segs[key]
            episodes.pop(key)

    daily = [[0.0, 0.0, 0.0] for _ in range(ndays)]
    monthly = defaultdict(Counter)
    conflict_h = 0.0
    sections = []
    for key, sg in segs.items():
        hrs = [[0.0, 0.0, 0.0] for _ in range(ndays)]
        chrs = [Counter() for _ in range(ndays)]
        conf = [0.0] * ndays
        for a, b, s, c, cf in sg:
            t = a
            while t < b:
                d = (t - day0).days
                nxt = min(b, day0 + timedelta(days=d + 1))
                h = H(t, nxt)
                hrs[d][s - 1] += h
                chrs[d][c] += h
                if cf:
                    conf[d] += h
                t = nxt
        for d in range(ndays):
            for k in range(3):
                daily[d][k] += hrs[d][k] / 24
            month = (day0 + timedelta(days=d)).strftime("%Y-%m")
            for c, h in chrs[d].items():
                monthly[month][c] += h / 24
        conflict_h += sum(conf)
        sections.append({"key": key, "hrs": hrs, "chrs": chrs, "conf": conf,
                         "bad_h": sum(map(sum, hrs)), "total_h": sum(h[2] for h in hrs)})

    # peak concurrency
    sweep = sorted([(a, 1) for sg in segs.values() for a, *_ in sg] + [(b, -1) for sg in segs.values() for _, b, *_ in sg],
                   key=lambda x: (x[0], x[1]))
    cur = peak = 0
    peak_at = None
    for t, dv in sweep:
        cur += dv
        if cur > peak:
            peak, peak_at = cur, t

    # episode durations by dominant cause, and full-closure durations on the passes
    durations = []
    for key, eps in episodes.items():
        for ep in eps:
            a, b = ep[0][0], ep[-1][1]
            h = H(a, b)
            if h < MIN_EPISODE_H:
                continue
            c = Counter()
            for sa, sb, s, cz, cf in segs[key]:
                if sa >= a and sb <= b:
                    c[cz] += H(sa, sb)
            durations.append({"c": NAMES.index(c.most_common(1)[0][0]), "h": round(h, 1),
                              "open": b == end, "a": a.date().isoformat(), "s": f"RN {key[1]} · {key[0]} · {key[2]}"})
    passes = []
    for region, ruta, tramo, label in PASSES:
        closures = []
        for ep in episodes.get((region, ruta, tramo), []):
            run = None  # consecutive CORTE TOTAL segments inside the episode
            for a, b, s, est, obs in ep + [(None, None, 0, None, None)]:
                if s == 3:
                    run = [run[0] if run else a, b]
                elif run:
                    if H(*run) >= MIN_EPISODE_H:
                        closures.append({"h": round(H(*run), 1), "a": run[0].date().isoformat(), "open": run[1] == end})
                    run = None
        passes.append({"label": label, "closures": closures})

    sections.sort(key=lambda s: -s["bad_h"])
    top = []
    for s in sections[:40]:
        sev, frac, cz, cf = [], [], [], []
        for d in range(ndays):
            h = s["hrs"][d]
            tot = sum(h)
            if tot == 0:
                sev.append("0"), frac.append("0"), cz.append("."), cf.append("0")
                continue
            sev.append(str(max(range(3), key=lambda k: h[k]) + 1))  # state held longest that day
            frac.append(str(min(9, round(tot / 24 * 9))))
            cz.append(str(NAMES.index(s["chrs"][d].most_common(1)[0][0])))
            cf.append("1" if s["conf"][d] > 0 else "0")
        top.append({"region": s["key"][0], "ruta": s["key"][1], "tramo": s["key"][2],
                    "days_bad": round(s["bad_h"] / 24, 1), "days_total": round(s["total_h"] / 24, 1),
                    "sev": "".join(sev), "frac": "".join(frac), "cause": "".join(cz), "conf": "".join(cf)})

    # totals for every affected section, for the map: [region, ruta, tramo, days not open, days closed, cause]
    totals = []
    for s in sections:
        cz = Counter()
        for c in s["chrs"]:
            cz.update(c)
        totals.append([*s["key"], round(s["bad_h"] / 24, 1), round(s["total_h"] / 24, 1),
                       NAMES.index(cz.most_common(1)[0][0])])

    out = {
        "start": day0.date().isoformat(), "end": end.isoformat(), "causes": NAMES,
        "daily": [[round(v, 2) for v in d] for d in daily],
        "monthly": {m: {c: round(v, 1) for c, v in cs.items()} for m, cs in sorted(monthly.items())},
        "top": top, "sections": totals, "permanent": permanent, "durations": durations, "passes": passes,
        "n_sections_affected": len(sections),
        "peak": {"n": peak, "at": peak_at.isoformat()},
        "total_closed_days": round(sum(d[2] for d in daily)),
        "conflict_days": round(conflict_h / 24),
        "min_episode_h": MIN_EPISODE_H,
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))

    tot = Counter()
    for c in monthly.values():
        tot.update(c)
    all_h = sum(tot.values())
    print(f"days={ndays} sections={len(sections)} permanent={[(p['ruta'], p['region']) for p in permanent]}")
    print(f"peak={peak} at {peak_at}; closed section-days={out['total_closed_days']}; conflict section-days={out['conflict_days']}")
    print("causes:", [(c, round(v), f"{v / all_h:.0%}") for c, v in tot.most_common()])
    print(f"episodes kept={len(durations)}; passes:", [(p["label"], len(p["closures"])) for p in passes])


if __name__ == "__main__":
    main()
