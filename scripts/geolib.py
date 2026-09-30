"""Small pure-Python geometry helpers for geometry.py (no GIS dependencies)."""
import math

R_KM = 6371.0088


def hav(a, b):
    """Great-circle distance in km between two (lon, lat) points."""
    p1, p2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_KM * math.asin(math.sqrt(h))


def xy(p, lat0):
    """Local equirectangular projection to km, good enough for distances of a few km."""
    return (math.radians(p[0]) * R_KM * math.cos(math.radians(lat0)), math.radians(p[1]) * R_KM)


def seg_dist(p, a, b):
    """Distance in km from p to segment ab, and the fraction along ab of the closest point."""
    lat0 = p[1]
    px, py = xy(p, lat0)
    ax, ay = xy(a, lat0)
    bx, by = xy(b, lat0)
    dx, dy = bx - ax, by - ay
    d2 = dx * dx + dy * dy
    t = 0.0 if d2 == 0 else max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / d2))
    return math.hypot(px - ax - t * dx, py - ay - t * dy), t


def in_ring(p, ring):
    x, y = p
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


class Polys:
    """Named multipolygons with bounding boxes, for point-in-polygon lookups."""

    def __init__(self, features, name_key):
        self.items = []
        for f in features:
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            for poly in polys:
                ring = poly[0]
                xs, ys = [c[0] for c in ring], [c[1] for c in ring]
                self.items.append((f["properties"][name_key], (min(xs), min(ys), max(xs), max(ys)), poly))
        self.last = None

    def _hit(self, p, item):
        _, (x0, y0, x1, y1), poly = item
        if not (x0 <= p[0] <= x1 and y0 <= p[1] <= y1):
            return False
        return in_ring(p, poly[0]) and not any(in_ring(p, h) for h in poly[1:])

    def find(self, p):
        if self.last and self._hit(p, self.last):
            return self.last[0]
        for item in self.items:
            if self._hit(p, item):
                self.last = item
                return item[0]
        return None


class Line:
    """A route as a list of parts; positions are km of chainage measured along the drawn line.

    Gaps between parts (ferries, stretches through Chile) add no chainage.
    """

    def __init__(self, parts):
        self.parts = [p for p in parts if len(p) > 1]
        self.pts, self.cum, self.breaks = [], [], []  # breaks: index of first vertex of each part after the first
        d = 0.0
        for part in self.parts:
            if self.pts:
                self.breaks.append(len(self.pts))
            for i, c in enumerate(part):
                if i:
                    d += hav(part[i - 1], c)
                self.pts.append((c[0], c[1]))
                self.cum.append(d)
        self.length = d
        self._break_set = set(self.breaks)
        ys = [p[1] for p in self.pts]
        xs = [p[0] for p in self.pts]
        self.bbox = (min(xs), min(ys), max(xs), max(ys))

    def _chunks(self, size=48):
        if not hasattr(self, "_ch"):
            self._ch = []
            for i in range(0, len(self.pts) - 1, size):
                j = min(len(self.pts) - 1, i + size)
                xs = [p[0] for p in self.pts[i:j + 1]]
                ys = [p[1] for p in self.pts[i:j + 1]]
                self._ch.append((i, j, min(xs), min(ys), max(xs), max(ys)))
        return self._ch

    def locate(self, p, lo=None, hi=None):
        """Closest point of the line to p: (distance km, chainage km). Optionally limited to chainage [lo, hi]."""
        best = (1e9, 0.0)
        kx = math.cos(math.radians(p[1])) * 111.2
        order = []
        for i0, i1, x0, y0, x1, y1 in self._chunks():
            if lo is not None and self.cum[i1] < lo or hi is not None and self.cum[i0] > hi:
                continue
            dx = max(x0 - p[0], 0, p[0] - x1) * kx
            dy = max(y0 - p[1], 0, p[1] - y1) * 111.2
            order.append((max(dx, dy) * 0.98, i0, i1))  # lower bound on the distance to the chunk
        order.sort()
        for bound, i0, i1 in order:
            if bound > best[0]:
                break
            for i in range(i0, i1):
                if (i + 1) in self._break_set:
                    continue
                d, t = seg_dist(p, self.pts[i], self.pts[i + 1])
                if d < best[0]:
                    s = self.cum[i] + t * (self.cum[i + 1] - self.cum[i])
                    if (lo is None or s >= lo) and (hi is None or s <= hi):
                        best = (d, s)
        return best

    def point_at(self, s):
        import bisect
        s = max(0.0, min(self.length, s))
        i = bisect.bisect_right(self.cum, s) - 1
        i = max(0, min(len(self.pts) - 2, i))
        if (i + 1) in self._break_set:
            return self.pts[i]
        a, b = self.pts[i], self.pts[i + 1]
        span = self.cum[i + 1] - self.cum[i]
        t = 0 if span == 0 else (s - self.cum[i]) / span
        return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))

    def cut(self, s0, s1):
        """Sub-line between chainages s0 < s1, as a list of parts."""
        import bisect
        out, cur = [], [self.point_at(s0)]
        i = bisect.bisect_right(self.cum, s0)
        while i < len(self.pts) and self.cum[i] < s1:
            if i in self._break_set:
                if len(cur) > 1:
                    out.append(cur)
                cur = []
            cur.append(self.pts[i])
            i += 1
        if i < len(self.pts) and i not in self._break_set or i >= len(self.pts):
            cur.append(self.point_at(s1))
        if len(cur) > 1:
            out.append(cur)
        return out


def simplify(pts, tol_km):
    """Douglas-Peucker with tolerance in km."""
    if len(pts) < 3:
        return list(pts)
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        dmax, imax = 0.0, -1
        for i in range(a + 1, b):
            d, _ = seg_dist(pts[i], pts[a], pts[b])
            if d > dmax:
                dmax, imax = d, i
        if dmax > tol_km:
            keep[imax] = True
            stack.append((a, imax))
            stack.append((imax, b))
    return [p for p, k in zip(pts, keep) if k]


def length(parts):
    return sum(hav(p[i], p[i + 1]) for p in parts for i in range(len(p) - 1))
