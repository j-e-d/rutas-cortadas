"""Extract status-change history from estadorutas git history into CSVs.

Usage: history.py <estadorutas clone> <output dir>

Outputs:
  rutas_changes.csv    one row per section per change in estado/calzada/detalle/observaciones
  rutas_snapshots.csv  one row per commit: timestamp + count of sections per estado

region is the Vialidad district for schema=old (before 2024-12-01), the province for schema=new.
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(sys.argv[1])
FILE = "estado-rutas.json"
OUT = Path(sys.argv[2])
TAG = re.compile(r"<[^>]+>")
# Before 2024-12-01 the sheet had no estado column (keyed by Vialidad district, status in free-text
# "detalle"), so estado is inferred from keywords for that era.
INFER = [
    ("CORTE TOTAL", re.compile(r"CERRAD|CORTAD|CORTE TOTAL|INTRANSITABLE|NO HABILITAD", re.I)),
    ("CORTE PARCIAL", re.compile(r"CORTE PARCIAL|MEDIA CALZADA|PASO ALTERNADO|CARRIL", re.I)),
    ("RESTRINGIDA", re.compile(r"RESTRING|CADENAS|4\s*X\s*4|SOLO VEH", re.I)),
]


def infer(text):
    for estado, rx in INFER:
        if rx.search(text):
            return estado
    return "HABILITADA"


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout


def parse(raw):
    data = json.loads(raw)
    rows = data["values"] if isinstance(data, dict) else data
    schema = "old" if rows and rows[0][0] == "filtro-distrito" else "new"
    out = {}
    for r in rows[2:]:
        if len(r) < 4:
            continue
        r = [" ".join(x.split()) for x in r] + [""] * 9
        key = (r[0], r[1], r[2])
        if schema == "old":  # distrito, ruta, tramo, calzada, detalle, observaciones, actualizacion
            out[key] = {"estado": infer(r[4]), "calzada": r[3], "km": "", "detalle": r[4],
                        "observaciones": r[5], "actualizado": r[6]}
        else:  # provincia, ruta, tramo, estado, calzada, km, conoce-mas, observaciones, actualizado
            out[key] = {"estado": TAG.sub("", r[3]).strip(), "calzada": r[4], "km": r[5], "detalle": "",
                        "observaciones": r[7], "actualizado": r[8]}
    return schema, out


def main():
    commits = [l.split(" ", 1) for l in git("log", "--reverse", "--format=%H %cI", "--", FILE).splitlines()]
    prev = {}
    changes, snaps, bad = [], [], 0
    for sha, ts in commits:
        try:
            schema, cur = parse(git("show", f"{sha}:{FILE}"))
        except (json.JSONDecodeError, KeyError, subprocess.CalledProcessError):
            bad += 1
            continue
        if not cur:
            bad += 1
            continue
        if snaps and snaps[-1]["schema"] != schema:
            prev = {}  # keys aren't comparable across schemas; restart diffing
        counts = {}
        for s in cur.values():
            counts[s["estado"]] = counts.get(s["estado"], 0) + 1
        snaps.append({"ts": ts, "commit": sha[:8], "schema": schema, "sections": len(cur), **counts})
        for key, s in cur.items():
            p = prev.get(key)
            if p is None or any(p[f] != s[f] for f in ("estado", "calzada", "detalle", "observaciones")):
                changes.append({"ts": ts, "commit": sha[:8], "schema": schema, "region": key[0], "ruta": key[1], "tramo": key[2],
                                "event": "new" if p is None else "change",
                                "estado_prev": p["estado"] if p else "", **s})
        for key in prev.keys() - cur.keys():
            changes.append({"ts": ts, "commit": sha[:8], "schema": schema, "region": key[0], "ruta": key[1], "tramo": key[2],
                            "event": "removed", "estado_prev": prev[key]["estado"], "estado": "", "calzada": "",
                            "km": "", "detalle": "", "observaciones": "", "actualizado": ""})
        prev = cur

    with open(OUT / "rutas_changes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(changes[0].keys()))
        w.writeheader()
        w.writerows(changes)
    estados = sorted({k for s in snaps for k in s} - {"ts", "commit", "schema", "sections"})
    with open(OUT / "rutas_snapshots.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "commit", "schema", "sections", *estados], restval=0)
        w.writeheader()
        w.writerows(snaps)
    print(f"commits={len(commits)} parsed={len(snaps)} unparseable={bad} change_rows={len(changes)}")


if __name__ == "__main__":
    main()
