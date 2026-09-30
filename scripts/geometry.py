"""One-off: cut Vialidad's route centrelines into the sections of the road-status table.

Usage: geometry.py fetch                                  download the source layers to geodata/raw/
       geometry.py build <estadorutas clone> <rutas_changes.csv>
                                                          write site/geo.json and geodata/match_report.md

Runs locally, not in CI; site/geo.json is committed. Standard library only.

Sources (all public government layers):
  SIG Vial, Dirección Nacional de Vialidad (sigvial.vialidad.gob.ar): Red Vial Nacional 2025,
    Postes Kilométricos 2025, Intersecciones 2025.
  Instituto Geográfico Nacional (wms.ign.gob.ar): provincia, localidad_bahra, bahra_paraje.

The status table has no coordinates or progresivas, only a section name ("Cañuelas - Azul") and a
length in km. Each endpoint name is turned into candidate positions along the route ("anchors"):
province borders, junctions listed in DNV's intersection layer, geometric junctions with other
national routes, BAHRA place names near the road, explicit km posts. A dynamic program then picks
the set of anchors that is in order along the route and agrees with the table's km lengths.
Sections with both ends anchored are "alta"; sections placed by interpolating or measuring km from
a neighbouring anchor are "media"; anything else is left out and listed in the report.
"""
import csv
import difflib
import json
import re
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from geolib import Line, Polys, hav, length, simplify  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "geodata" / "raw"
OUT = ROOT / "site" / "geo.json"
REPORT = ROOT / "geodata" / "match_report.md"
PRIVATE = ROOT / "geodata" / "private"

LAYERS = {
    "sv_red.json": ("https://sigvial.vialidad.gob.ar/geoserver/wfs", "dnv:Red_Vial_Ncional2025"),
    "sv_postes.json": ("https://sigvial.vialidad.gob.ar/geoserver/wfs", "dnv:Postes_Kilometricos_2025"),
    "sv_inter.json": ("https://sigvial.vialidad.gob.ar/geoserver/wfs", "dnv:Intersecciones_2025"),
    "provincia.json": ("https://wms.ign.gob.ar/geoserver/ign/ows", "ign:provincia"),
    "localidad_bahra.json": ("https://wms.ign.gob.ar/geoserver/ign/ows", "ign:localidad_bahra"),
    "bahra_paraje.json": ("https://wms.ign.gob.ar/geoserver/ign/ows", "ign:bahra_paraje"),
}

DEBUG = False
SIMPLIFY_KM = 0.06      # road lines
OUTLINE_KM = 1.2        # province outlines
MIN_ISLAND_KM = 60      # drop outline rings with a shorter perimeter
PLACE_MAX_KM = 12       # a named place counts if it is this close to the road
JUNCTION_KM = 0.3       # two national routes "meet" when their lines come this close

# Table route names that are spelled differently in DNV's layer. Each was checked by province and length.
ALIASES = {"COMPL A": "24CA", "COMPL B": "24CB", "COMPL I": "24CI", "COMPL J": "24CJ", "COMPL K": "24CK",
           "IV66": "1V66", "1V143": "V143", "AU. RICCHERI": "A002"}
ABBR = {"gral": "general", "cnel": "coronel", "sta": "santa", "sto": "santo", "pto": "puerto", "va": "villa",
        "cte": "comandante", "gdor": "gobernador", "gob": "gobernador", "ing": "ingeniero", "tte": "teniente",
        "cap": "capitan", "pje": "paraje", "cnia": "colonia", "col": "colonia", "sgo": "santiago", "dr": "doctor",
        "pcia": "presidencia", "ea": "estancia", "est": "estancia", "s": "san", "int": "", "emp": "",
        "empalme": "", "interseccion": "", "acc": "", "acceso": "", "accesos": "", "ex": "", "rot": "rotonda"}
PHRASES = [(r"\bs\W*a\W+oeste\b", "san antonio oeste"), (r"\bs\W*s\W+de jujuy\b", "san salvador de jujuy"),
           (r"\bs\W*m\W+de tucuman\b", "san miguel de tucuman"), (r"\bcaba\b", "ciudad autonoma de buenos aires"),
           (r"\bcdro\W+rivadavia\b", "comodoro rivadavia"), (r"\bs\W*c\W+de bariloche\b", "san carlos de bariloche")]
STOP = {"a", "al", "con", "c", "de", "del", "la", "las", "los", "el", "y", "en", "rn", "rp", "n", "nro", "ruta", "km"}
COUNTRIES = {"chile", "bolivia", "paraguay", "brasil", "uruguay"}
REF = re.compile(r"\bR\.?\s*([NP])\.?\s*(?:N\s*[°ºª]\s*|N[RrOo]\.?\s*|\.\s*)?((?:[A-Z]\s?-?\s?)?\d+[A-Z]?\d*)", re.I)
KM = re.compile(r"\bkm\.?\s*(\d+(?:[.,]\d+)?)", re.I)
BORDER = re.compile(r"^\s*(lte|l[ií]mite|lim)\b\.?\s*(con\b|c/)?\s*(.*)$", re.I)


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def tokens(s):
    """Name tokens of an endpoint or description: folded, abbreviations expanded, route refs and noise removed."""
    s = fold(REF.sub(" ", KM.sub(" ", s)))
    for rx, rep in PHRASES:
        s = re.sub(rx, rep, s)
    out = []
    for t in re.split(r"[^a-z0-9ñ]+", s):
        t = ABBR.get(t, t)
        if t and t not in STOP and not t.isdigit():
            out.append(t)
    return tuple(out)


def refs(s):
    """Route references in a text, as ('N', '229') / ('P', '51') / ('N', 'A5')."""
    out = set()
    for kind, num in REF.findall(s):
        num = re.sub(r"[\s-]", "", num.upper())
        m = re.fullmatch(r"([A-Z]?)0*(\d+)", num)
        out.add((kind.upper(), m.group(1) + m.group(2) if m else num))
    return out


def route_code(r):
    r = r.strip().upper()
    r = ALIASES.get(r, r).replace("-", "").replace(" ", "")
    if r.isdigit():
        return r.zfill(4)
    m = re.fullmatch(r"A(\d+)", r)
    return "A" + m.group(1).zfill(3) if m else r


def ref_code(ref):
    """DNV route code for a ('N', ...) reference."""
    return route_code(ref[1])


def same_name(a, b):
    ta, tb = tokens(a), tokens(b)
    ra, rb = refs(a), refs(b)
    if ra and rb:
        return bool(ra & rb)
    if not ta or not tb:
        return False
    if ta == tb or set(ta) <= set(tb) or set(tb) <= set(ta):
        return True
    return difflib.SequenceMatcher(None, " ".join(ta), " ".join(tb)).ratio() >= 0.8


def split_tramo(t):
    parts = [p.strip() for p in re.split(r"\s+-\s*|\s*-\s+", t) if p.strip()]
    if len(parts) == 1 and t.count("-") == 1:
        a, b = t.split("-")
        if len(re.sub(r"[^A-Za-zÀ-ÿ]", "", a)) >= 4 and len(re.sub(r"[^A-Za-zÀ-ÿ]", "", b)) >= 4 and not REF.search(t[max(0, len(a) - 6):len(a) + 4]):
            parts = [a.strip(), b.strip()]
    return parts


def fetch():
    RAW.mkdir(parents=True, exist_ok=True)
    for name, (base, layer) in LAYERS.items():
        q = urllib.parse.urlencode({"service": "WFS", "version": "1.0.0", "request": "GetFeature", "typeName": layer,
                                    "outputFormat": "application/json", "srsName": "EPSG:4326"})
        print("fetching", layer)
        with urllib.request.urlopen(f"{base}?{q}", timeout=600) as r:
            (RAW / name).write_bytes(r.read())


def load(name):
    return json.loads((RAW / name).read_text())["features"]


# ---------------------------------------------------------------------------------------------- inputs

def read_table(raw):
    data = json.loads(raw)
    rows = data["values"] if isinstance(data, dict) else data
    out = []
    for r in rows[2:]:
        if len(r) < 4:
            continue
        r = [" ".join(x.split()) for x in r] + [""] * 9
        try:
            km = float(r[5].replace(",", "."))
        except ValueError:
            km = None
        out.append({"key": (r[0], r[1], r[2]), "km": km})
    return out


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


def historical_groups(repo, changes, current_keys):
    """Sections that left the table but had affected time: their (region, ruta) group as last published."""
    last, affected = {}, set()
    for r in csv.DictReader(open(changes)):
        if r["schema"] != "new":
            continue
        key = (r["region"], r["ruta"], r["tramo"])
        if key in current_keys or not key[2]:
            continue
        if r["event"] == "removed":
            last[key] = r["commit"]
        elif r["estado"] not in ("HABILITADA", ""):
            affected.add(key)
    groups = []
    for commit in sorted({last[k] for k in affected if k in last}):
        table = None
        for back in range(1, 6):
            try:
                table = read_table(git(repo, "show", f"{commit}~{back}:estado-rutas.json"))
            except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError):
                continue
            if table:
                break
        if not table:
            continue
        want = {k for k in affected if last.get(k) == commit}
        for g in {(k[0], k[1]) for k in want}:
            secs = [s for s in table if s["key"][:2] == g]
            if any(s["key"] in want for s in secs):
                groups.append((secs, want))
    return groups


class World:
    def __init__(self):
        self.lines = {}
        for f in load("sv_red.json"):
            p = f["properties"]
            if p["Sentido"] == "A":
                self.lines[p["RTN"]] = Line([[c[:2] for c in part] for part in f["geometry"]["coordinates"]])
        provs = load("provincia.json")
        self.prov_raw = provs
        # coarse copy for point-in-polygon
        coarse = []
        for f in provs:
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            keep = [[[c[:2] for c in ring[::max(1, len(ring) // 4000)]] + [ring[0][:2]] for ring in poly[:1]]
                    for poly in polys if len(poly[0]) > 200]
            coarse.append({"properties": f["properties"], "geometry": {"type": "MultiPolygon", "coordinates": keep}})
        self.polys = Polys(coarse, "nam")
        self.runs = {}
        self.inter = defaultdict(list)
        for f in load("sv_inter.json"):
            p = f["properties"]
            if p["descripcion"] and f["geometry"]:
                self.inter[p["cod_ruta"]].append((p["descripcion"], tuple(f["geometry"]["coordinates"][:2])))
        self.posts = defaultdict(list)
        for f in load("sv_postes.json"):
            p = f["properties"]
            self.posts[p["cod_ruta"]].append((p["progresiva"], tuple(f["geometry"]["coordinates"][:2])))
        self.places = defaultdict(list)
        for name in ("localidad_bahra.json", "bahra_paraje.json"):
            for f in load(name):
                p = f["properties"]
                t = tokens(p["fna"] or "")
                if t:
                    self.places[prov_name(p["nom_pcia"])].append((t, (float(p["long_gd"]), float(p["lat_gd"]))))
        self._post_s = {}
        self._junction = {}

    def province_runs(self, code):
        """[(province, s0, s1)] along the line; CABA counts as Buenos Aires."""
        if code not in self.runs:
            line, runs, cur = self.lines[code], [], None
            at = lambda i: prov_name(self.polys.find(line.pts[i]) or "")
            # test a vertex every ~1 km, then bisect to find where the province changes
            idx, last_s = [0], 0.0
            for i, s in enumerate(line.cum):
                if s - last_s >= 1.0 or i == len(line.cum) - 1:
                    idx.append(i)
                    last_s = s
            prev_i = None
            for i in idx:
                name = at(i) or cur
                if name != cur:
                    a, b = (prev_i if prev_i is not None else i), i
                    while b - a > 1:
                        m = (a + b) // 2
                        if (at(m) or cur) == cur:
                            a = m
                        else:
                            b = m
                    s = line.cum[b]
                    if runs:
                        runs[-1][2] = s
                    runs.append([name, s, s])
                    cur = name
                if runs:
                    runs[-1][2] = line.cum[i]
                prev_i = i
            self.runs[code] = [tuple(r) for r in runs if r[0]]
        return self.runs[code]

    def post_chainage(self, code, km):
        """Chainage of a progresiva, interpolated between the two nearest posts that lie on the line."""
        if code not in self._post_s:
            line, ps = self.lines[code], []
            for prog, pt in sorted(self.posts.get(code, [])):
                d, s = line.locate(pt)
                if d < 0.5:
                    ps.append((prog, s))
            self._post_s[code] = ps
        ps = self._post_s[code]
        for (p0, s0), (p1, s1) in zip(ps, ps[1:]):
            if p0 <= km <= p1 and p1 - p0 <= 150 and p1 > p0 and abs((s1 - s0) - (p1 - p0)) <= 0.1 * (p1 - p0) + 1:
                return s0 + (s1 - s0) * (km - p0) / (p1 - p0)
        return None

    def junctions(self, code, other, lo, hi):
        """Chainages on `code` where national route `other` joins or leaves it."""
        key = (code, other)
        if key not in self._junction:
            line, o = self.lines[code], self.lines.get(other)
            hits = []
            if o:
                x0, y0, x1, y1 = line.bbox
                last = -1.0
                for p, so in zip(o.pts, o.cum):
                    if so - last >= 0.15 and x0 - .02 <= p[0] <= x1 + .02 and y0 - .02 <= p[1] <= y1 + .02:
                        last = so
                        d, s = line.locate(p)
                        if d < JUNCTION_KM:
                            hits.append(s)
                for p in (o.pts[0], o.pts[-1]):  # routes that end at a junction without sharing a vertex
                    d, s = line.locate(p)
                    if d < 1.0:
                        hits.append(s)
            hits.sort()
            clusters = []
            for s in hits:
                if clusters and s - clusters[-1][1] < 3:
                    clusters[-1][1] = s
                else:
                    clusters.append([s, s])
            out = []
            for a, b in clusters:
                out += [(a + b) / 2] if b - a < 1.5 else [a, b]
            self._junction[key] = out
        return [s for s in self._junction[key] if lo - 1 <= s <= hi + 1]


def prov_name(n):
    t = fold(n or "")
    if t.startswith("tierra del fuego"):
        return "tierra del fuego"
    if t.startswith("ciudad autonoma"):
        return "buenos aires"
    return t.replace("sgo.", "santiago").strip()


PROV_TOKENS = None


def border_target(text):
    """Province or country named in 'Lte. con X', folded; None if this is not a border name."""
    m = BORDER.match(text)
    if not m:
        return None
    t = " ".join(tokens(m.group(3)))
    return t or None


# ---------------------------------------------------------------------------------------------- matching

def anchors_for(world, code, prov, name, lo, hi, runs):
    """Candidate (chainage, weight, kind) for one endpoint name, inside the group's hull [lo, hi]."""
    line, out = world.lines[code], []
    target = border_target(name)
    if target:
        for i, (p, s0, s1) in enumerate(runs):
            if p != prov:
                continue
            for j, s in ((i - 1, s0), (i + 1, s1)):
                other = " ".join(tokens(runs[j][0])) if 0 <= j < len(runs) else None
                if other and (other == target or target in other or other in target):
                    out.append((s, 3.0, "límite"))
        if not out and (set(target.split()) & COUNTRIES or "internacional" in target):
            for s in (0.0, line.length):
                if lo - 1 <= s <= hi + 1:
                    out.append((s, 2.5, "frontera"))
        return out
    rf, tk = refs(name), tokens(name)
    for kmtxt in KM.findall(name):
        s = world.post_chainage(code, float(kmtxt.replace(",", ".")))
        if s is not None and lo - 1 <= s <= hi + 1:
            out.append((s, 2.5, "km"))
    for desc, pt in world.inter.get(code, []):
        drefs, dtok = refs(desc), set(tokens(desc))
        by_ref = bool(rf & drefs)
        by_name = bool(tk) and not rf and all(t in dtok for t in tk) and any(len(t) >= 4 for t in tk)
        if by_ref or by_name:
            d, s = line.locate(pt, lo - 1, hi + 1)
            if d < 1.0:
                out.append((s, 3.0 if by_ref else 2.0, "intersección DNV"))
    for r in rf:
        if r[0] == "N" and ref_code(r) != code:
            for s in world.junctions(code, ref_code(r), lo, hi):
                out.append((s, 2.5, "cruce de rutas"))
    # place names; a parenthetical or a name after a route ref also counts ("Emp. RN 3 (Chimen Aike)")
    if tk and any(len(t) >= 4 for t in tk):
        joined = " ".join(tk)
        for ptok, pt in world.places.get(prov, []):
            if ptok == tk:
                q = 1.0
            elif set(tk) <= set(ptok) or set(ptok) <= set(tk) and len(ptok) * 2 >= len(tk):
                q = 0.8
            elif abs(len(joined) - len(" ".join(ptok))) <= 3 and difflib.SequenceMatcher(None, joined, " ".join(ptok)).ratio() >= 0.86:
                q = 0.7
            else:
                continue
            d, s = line.locate(pt, lo - 1, hi + 1)
            if d <= PLACE_MAX_KM:
                out.append((s, (1.0 + q) * (1 - d / (2 * PLACE_MAX_KM)) * (0.6 if rf else 1.0), "localidad"))
    # collapse near-duplicates, keeping the heaviest
    out.sort(key=lambda c: -c[1])
    kept = []
    for c in out:
        if all(abs(c[0] - k[0]) > 0.5 for k in kept):
            kept.append(c)
    return kept[:8]


def place_group(world, secs):
    """Place one (province, route) group. Returns {key: result dict}."""
    region, ruta = secs[0]["key"][:2]
    code, prov = route_code(ruta), prov_name(region)
    res = {s["key"]: {"why": None} for s in secs}

    def fail(why, only=None):
        for s in secs:
            if (only is None or s["key"] in only) and "s0" not in res[s["key"]]:
                res[s["key"]]["why"] = why
        return res

    if code not in world.lines:
        return fail("la ruta no está en la capa de Vialidad")
    line, runs = world.lines[code], world.province_runs(code)
    mine = [r for r in runs if r[0] == prov]
    if not mine:
        return fail("la traza de Vialidad no pasa por esta provincia")
    lo, hi = min(r[1] for r in mine), max(r[2] for r in mine)

    # nodes: endpoint names, shared between consecutive sections when the names agree
    nodes, sec_nodes = [], []  # node = {"names": [...], "gap_before": bool}
    for i, s in enumerate(secs):
        parts = split_tramo(s["key"][2])
        start = parts[:-1][:2] if len(parts) > 1 else []
        end = parts[1:][-2:] if len(parts) > 1 else []
        if i and nodes:
            prev = nodes[-1]
            shared = (not start or not prev["names"]) or any(same_name(a, b) for a in start for b in prev["names"])
            # a border name can mean two places when the route leaves the province and comes back
            if shared and any(border_target(n) for n in start + prev["names"]) and len(mine) > 1:
                shared = False
        else:
            shared = False
        if shared:
            prev["names"] = [n for n in prev["names"] if any(same_name(n, a) for a in start)] or prev["names"] + start
            prev["named"] = prev["named"] and bool(start)
            a = len(nodes) - 1
        else:
            nodes.append({"names": start, "gap": i > 0, "named": bool(start)})
            a = len(nodes) - 1
        nodes.append({"names": end, "gap": False, "named": bool(end)})
        sec_nodes.append((a, len(nodes) - 1))

    # km between consecutive nodes: section length, or a gap of unknown length
    step = []  # step[n] describes the move from node n to n+1: ("sec", km) or ("gap", None)
    sec_of_step = {}
    for i, (a, b) in enumerate(sec_nodes):
        if i and sec_nodes[i - 1][1] != a:
            step.append(("gap", None))
        step.append(("sec", secs[i]["km"]))
        sec_of_step[len(step) - 1] = i
    assert len(step) == len(nodes) - 1

    cands = []  # (node, s, weight, kind)
    for n, node in enumerate(nodes):
        for name in node["names"]:
            for s, w, kind in anchors_for(world, code, prov, name, lo, hi, runs):
                cands.append((n, s, w, kind))
    # the ends of the province run, as weak anchors for the first and last node
    # (stronger when the node has no name and the route itself ends there: "Tunel Internacional")
    for n in (0, len(nodes) - 1):
        for s in (lo, hi):
            ends = not nodes[n]["named"] and (s < 0.5 or s > line.length - 0.5)
            cands.append((n, s, 2.6 if ends else 0.4, "fin de ruta" if ends else "extremo"))
            if ends:  # "X - Lte. Internacional" followed by "Paso Internacional": the pass section reaches the border
                near = n + 1 if n == 0 else n - 1
                cands = [c for c in cands if not (c[0] == near and c[3] == "frontera")]

    def between(n0, n1):
        """(sum of known km, all known?, has gap?) over the steps from node n0 to n1."""
        k, known, gap = 0.0, True, False
        for kind, km in step[n0:n1]:
            if kind == "gap":
                gap = True
            elif km is None:
                known = False
            else:
                k += km
        return k, known, gap

    def solve(o):
        cs = sorted(cands, key=lambda c: (c[0], o * c[1]))
        best = [c[2] for c in cs]
        back = [None] * len(cs)
        for j, cj in enumerate(cs):
            for i in range(j):
                ci = cs[i]
                if ci[0] >= cj[0]:
                    continue
                d = o * (cj[1] - ci[1])
                k, known, gap = between(ci[0], cj[0])
                if gap or not known:
                    pen = 0.2
                    if d < 0.85 * k - 2.5:
                        if min(ci[2], cj[2]) < 1.5:
                            continue
                        pen = 1.5
                else:
                    err = abs(d - k)
                    if d <= 0.05:
                        continue
                    if err > max(6.0, 0.4 * k):
                        # the table's km disagree with the names. Two well-identified ends outweigh a km
                        # figure (several are wrong in the table); the section is then flagged in the report.
                        if min(ci[2], cj[2]) < 1.5 or cj[0] - ci[0] > 1 and not k / 4 <= d <= k * 4:
                            continue
                        pen = 1.5
                    else:
                        pen = min(1.5, (err / max(2.5, 0.15 * k)) ** 2)
                v = best[i] + cj[2] - pen
                if v > best[j]:
                    best[j], back[j] = v, i
        j = max(range(len(cs)), key=lambda x: best[x])
        score, chosen = best[j], {}
        while j is not None:
            chosen[cs[j][0]] = cs[j]
            j = back[j]
        return score, chosen

    (sa, ca), (sb, cb) = solve(1), solve(-1)
    o, chosen = (1, ca) if sa + 0.25 >= sb else (-1, cb)
    if DEBUG:
        print(f"-- {region} RN {ruta}: hull {lo:.1f}-{hi:.1f} of {line.length:.1f}, o={o}, scores {sa:.1f}/{sb:.1f}")
        for n, node in enumerate(nodes):
            cs = [(round(c[1], 1), round(c[2], 1), c[3]) for c in cands if c[0] == n]
            print(f"   node {n} {node['names']} step={step[n] if n < len(step) else ''} chosen={chosen.get(n, ('', ''))[1:]} cands={cs}")
    strong = [c for c in chosen.values() if c[3] != "extremo"]
    if not strong and len(chosen) < 2:
        return fail("ningún extremo del grupo pudo ubicarse sobre la traza")

    # positions for every node: chosen anchors, then interpolation or km measured from an anchor
    pos = {n: c[1] for n, c in chosen.items()}
    how = {n: c[3] for n, c in chosen.items()}
    anchored = sorted(chosen)
    # one section with no km between two anchors takes whatever length is left over
    for a0, a1 in zip(anchored, anchored[1:]):
        k, known, gap = between(a0, a1)
        unknown = [n for n in range(a0, a1) if step[n] == ("sec", None)]
        rest = abs(pos[a1] - pos[a0]) - k
        if not gap and len(unknown) == 1 and a1 - a0 > 1 and rest > 0.5:
            step[unknown[0]] = ("sec", rest)
            secs[sec_of_step[unknown[0]]]["km_inferred"] = True
    for n in range(len(nodes)):
        if n in pos:
            continue
        left = max((a for a in anchored if a < n), default=None)
        right = min((a for a in anchored if a > n), default=None)
        okl = left is not None and between(left, n)[1:] == (True, False)
        okr = right is not None and between(n, right)[1:] == (True, False)
        if okl and okr:
            kl, kr = between(left, n)[0], between(n, right)[0]
            if kl + kr > 0:
                pos[n] = pos[left] + (pos[right] - pos[left]) * kl / (kl + kr)
                how[n] = "interpolado"
        elif okl:
            pos[n], how[n] = pos[left] + o * between(left, n)[0], "km desde ancla"
        elif okr:
            pos[n], how[n] = pos[right] - o * between(n, right)[0], "km desde ancla"
    # measured positions must stay on the province run and must not pass the next fixed node
    for n in sorted(pos):
        if how[n] != "km desde ancla":
            continue
        # (it may leave the province: some sections are listed under the neighbouring one)
        bad = not (-1 <= pos[n] <= line.length + 1)
        for a in anchored:
            if (a - n) * o * (pos[a] - pos[n]) < -3:
                bad = True
        if bad:
            del pos[n], how[n]

    spans = [tuple(sorted((pos[a], pos[b]))) for a, b in sec_nodes if a in pos and b in pos]
    for i, s in enumerate(secs):
        a, b = sec_nodes[i]
        r = res[s["key"]]
        if a not in pos or b not in pos:
            # a section that runs against the group's direction, or sits apart from it: place it on its own
            # if both ends are well identified, agree with its km, and it does not overlap a placed section
            best = None
            for ca in [c for c in cands if c[0] == a and c[2] >= 1.8 and (a not in chosen or c == chosen[a])]:
                for cb in [c for c in cands if c[0] == b and c[2] >= 1.8 and (b not in chosen or c == chosen[b])]:
                    d = abs(ca[1] - cb[1])
                    ok_km = s["km"] is None or abs(d - s["km"]) <= max(3.0, 0.2 * s["km"])
                    lo_, hi_ = sorted((ca[1], cb[1]))
                    free = all(min(hi_, y) - max(lo_, x) < 3 for x, y in spans)
                    if d > 0.2 and ok_km and free and (best is None or ca[2] + cb[2] > best[0]):
                        best = (ca[2] + cb[2], ca, cb)
            if best is None:
                r["why"] = "sin ancla en un extremo y sin tramo vecino ubicado para medir"
                continue
            pos[a], how[a], pos[b], how[b] = best[1][1], best[1][3], best[2][1], best[2][3]
            spans.append(tuple(sorted((pos[a], pos[b]))))
        s0, s1 = sorted((pos[a], pos[b]))
        s0, s1 = max(0.0, s0), min(line.length, s1)
        if s1 - s0 < 0.2:
            r["why"] = "los dos extremos caen en el mismo punto"
            continue
        if "km desde ancla" in (how[a], how[b]) and any(s0 < line.cum[k] < s1 for k in line.breaks):
            r["why"] = "medido en km desde un extremo, pero la traza de Vialidad se interrumpe en el medio"
            continue
        direct = {"límite", "frontera", "fin de ruta", "km", "intersección DNV", "cruce de rutas", "localidad"}
        both = how[a] in direct and how[b] in direct
        r.update(s0=s0, s1=s1, code=code, conf="alta" if both and s["km"] is not None else "media",
                 how=f"{how[a]} / {how[b]}", geo_km=s1 - s0)
        r.pop("why")
    return res


# ---------------------------------------------------------------------------------------------- output

def enc(pts):
    """Delta-encode a line as integers of 1e-4 degrees: [x0, y0, dx, dy, ...]."""
    out, px, py = [], 0, 0
    for x, y in pts:
        ix, iy = round(x * 1e4), round(y * 1e4)
        if out and ix == px and iy == py:
            continue
        out += [ix - px, iy - py]
        px, py = ix, iy
    return out


def outlines(world):
    rings = []
    for f in world.prov_raw:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            ring = [c[:2] for c in poly[0]]
            # mainland, Tierra del Fuego and Malvinas; the Antarctic sector and the South Atlantic islands fall
            # outside the map's extent
            if len(ring) < 40 or min(c[1] for c in ring) < -56.5 or min(c[0] for c in ring) > -52:
                continue
            ring = ring[::max(1, len(ring) // 20000)] + [ring[0]]
            if length([ring]) < MIN_ISLAND_KM:
                continue
            s = simplify(ring, OUTLINE_KM)
            if len(s) >= 4:
                rings.append(enc(s))
    return rings


def build(repo, changes):
    world = World()
    table = read_table((Path(repo) / "estado-rutas.json").read_text())
    current = {s["key"] for s in table}
    groups = defaultdict(list)
    for s in table:
        groups[s["key"][:2]].append(s)
    jobs = [(secs, None) for secs in groups.values()] + historical_groups(repo, changes, current)

    results, kms, old = {}, {}, set()
    for secs, want in jobs:
        res = place_group(world, secs)
        for s in secs:
            if want is None or s["key"] in want:
                results[s["key"]] = res[s["key"]]
                kms[s["key"]] = s["km"]
                if want is not None:
                    old.add(s["key"])

    out_secs, rows = [], []
    for key, r in results.items():
        km = kms[key]
        row = {"key": key, "km": km, "old": key in old, **r}
        if "s0" in r:
            parts = world.lines[r["code"]].cut(r["s0"], r["s1"])
            parts = [simplify(p, SIMPLIFY_KM) for p in parts]
            row["geo_km"] = length(parts)
            diff = None if km is None else row["geo_km"] - km
            row["flag"] = diff is not None and abs(diff) > max(3.0, 0.2 * km)
            measured = any(w in r["how"] for w in ("interpolado", "km desde ancla", "extremo"))
            if row["flag"] and measured and abs(diff) > 5 and not 1 / 1.5 <= row["geo_km"] / km <= 1.5:
                rows.append({"key": key, "km": km, "old": key in old,
                             "why": f"un extremo sin ancla y el largo no coincide ({row['geo_km']:.0f} km sobre la traza)"})
                continue
            if row["flag"] and r["conf"] == "alta":
                row["conf"] = "media"
            sec = {"k": list(key), "c": row["conf"][0], "l": [enc(p) for p in parts]}
            if key in old:
                sec["old"] = 1
            out_secs.append(sec)
        rows.append(row)

    geo = {"source": "Dirección Nacional de Vialidad, SIG Vial (Red Vial Nacional 2025); Instituto Geográfico Nacional",
           "scale": 1e4, "provinces": outlines(world), "sections": out_secs}
    OUT.write_text(json.dumps(geo, ensure_ascii=False, separators=(",", ":")))
    write_report(rows, world)
    crosscheck(rows, world)
    n = lambda c: sum(1 for r in rows if r.get("conf") == c)
    print(f"sections={len(rows)} alta={n('alta')} media={n('media')} sin ubicar={sum(1 for r in rows if 's0' not in r)} "
          f"geo.json={OUT.stat().st_size / 1024:.0f} KB")


def write_report(rows, world):
    lab = lambda r: f"RN {r['key'][1]} · {r['key'][0]} · {r['key'][2] or '(sin nombre)'}" + (" *(dado de baja)*" if r["old"] else "")
    placed = [r for r in rows if "s0" in r]
    alta, media = [r for r in placed if r["conf"] == "alta"], [r for r in placed if r["conf"] == "media"]
    missing = [r for r in rows if "s0" not in r]
    flagged = sorted((r for r in placed if r["flag"]), key=lambda r: -abs(r["geo_km"] - r["km"]))
    L = ["# Informe de ubicación de tramos", "",
         "Generado por `scripts/geometry.py build`. Cada tramo de la tabla de Vialidad se ubicó sobre la traza de la",
         "Red Vial Nacional 2025 (SIG Vial, DNV) buscando sus dos extremos.", "",
         f"- Tramos: {len(rows)}",
         f"- Ubicados con confianza alta (los dos extremos anclados y el largo coincide): {len(alta)}",
         f"- Ubicados por aproximación (interpolados o medidos en km desde un extremo anclado): {len(media)}",
         f"- Sin ubicar (no se dibujan): {len(missing)}",
         f"- Con diferencia grande entre el largo dibujado y los km de la tabla: {len(flagged)}", "",
         "## Sin ubicar", "", "| Tramo | km tabla | Motivo |", "|---|---|---|"]
    L += [f"| {lab(r)} | {'' if r['km'] is None else r['km']} | {r['why']} |" for r in sorted(missing, key=lambda r: r["key"])]
    L += ["", "## Diferencias de largo", "", "Largo dibujado contra km de la tabla, cuando difieren más de 3 km y más de 20%.", "",
          "| Tramo | km tabla | km dibujado | Extremos |", "|---|---|---|---|"]
    L += [f"| {lab(r)} | {r['km']} | {r['geo_km']:.1f} | {r['how']} |" for r in flagged]
    L += ["", "## Ubicados por aproximación", "", "| Tramo | km tabla | km dibujado | Extremos |", "|---|---|---|---|"]
    L += [f"| {lab(r)} | {'' if r['km'] is None else r['km']} | {r['geo_km']:.1f} | {r['how']} |" for r in sorted(media, key=lambda r: r["key"])]
    L += ["", "## Ubicados con confianza alta", "", "| Tramo | km tabla | km dibujado | Extremos |", "|---|---|---|---|"]
    L += [f"| {lab(r)} | {r['km']} | {r['geo_km']:.1f} | {r['how']} |" for r in sorted(alta, key=lambda r: r["key"])]
    REPORT.write_text("\n".join(L) + "\n")


def crosscheck(rows, world):
    """Private sanity check against rough third-party points. Never published; only distances are printed."""
    f = PRIVATE / "tramos_db.json"
    if not f.exists():
        return
    ref = {}
    for t in json.loads(f.read_text()):
        if t.get("Coordenadas"):
            pts = [tuple(map(float, c.split(",")))[::-1] for c in t["Coordenadas"].split("/") if "," in c]
            ref[(prov_name(t["NombreProvincia"]), t["NombreRuta"].strip(), fold(t["TramoDesnormalizado"] or "").strip())] = pts
    lines = []
    for r in rows:
        k = (prov_name(r["key"][0]), r["key"][1], fold(r["key"][2]).strip())
        if "s0" not in r or k not in ref:
            continue
        line = world.lines[r["code"]]
        ends = [line.point_at(r["s0"]), line.point_at(r["s1"])]
        rp = ref[k]
        d = max(min(hav(e, p) for p in (rp[0], rp[-1])) for e in ends)
        lines.append((d, r["conf"], " · ".join(r["key"]), r["how"]))
    lines.sort(reverse=True)
    (PRIVATE / "crosscheck.txt").write_text("\n".join(f"{d:7.1f} km  {c}  {k}  [{h}]" for d, c, k, h in lines) + "\n")
    for c in ("alta", "media"):
        ds = sorted(d for d, cc, *_ in lines if cc == c)
        if ds:
            print(f"crosscheck {c}: n={len(ds)} median={ds[len(ds) // 2]:.1f} km p90={ds[int(len(ds) * .9)]:.1f} km >15km={sum(d > 15 for d in ds)}")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "fetch":
        fetch()
    elif len(sys.argv) == 4 and sys.argv[1] == "build":
        build(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
