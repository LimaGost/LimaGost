import json, random
from shapely.geometry import shape, Point
from shapely.ops import unary_union

with open('/tmp/brazil.json') as f:
    gj = json.load(f)

polys = [shape(feat['geometry']) for feat in gj['features']]
brazil = unary_union(polys)

minx, miny, maxx, maxy = brazil.bounds
print("bounds:", minx, miny, maxx, maxy)

# target drawing area inside the SVG (left "VISUAL.MAP" panel)
PAD = 6
AREA_X0, AREA_Y0 = 0, 0
AREA_W, AREA_H = 380, 460

# preserve aspect ratio, fit inside area with padding
geo_w = maxx - minx
geo_h = maxy - miny
scale = min((AREA_W - 2*PAD) / geo_w, (AREA_H - 2*PAD) / geo_h)
draw_w = geo_w * scale
draw_h = geo_h * scale
offset_x = AREA_X0 + (AREA_W - draw_w) / 2
offset_y = AREA_Y0 + (AREA_H - draw_h) / 2

def to_svg(lon, lat):
    x = offset_x + (lon - minx) * scale
    y = offset_y + (maxy - lat) * scale  # flip vertically
    return x, y

random.seed(42)

# grid resolution in geo-degrees
step_lon = geo_w / 68
step_lat = geo_h / 68

dots = []
lat = miny
row = 0
while lat <= maxy:
    lon = minx
    col = 0
    while lon <= maxx:
        # slight wave offset per row for an organic "scan line" feel
        wave = 0.0
        p = Point(lon, lat)
        if brazil.contains(p) or brazil.distance(p) < step_lon * 0.15:
            x, y = to_svg(lon, lat)
            # distance-based radius: slightly smaller near the coastline (edge) for a soft falloff
            inside = brazil.contains(p)
            r = 1.15 if inside else 0.65
            jitter = random.uniform(-0.25, 0.25)
            dots.append((round(x + jitter, 2), round(y + jitter*0.6, 2), r))
        lon += step_lon
        col += 1
    lat += step_lat
    row += 1

print("dot count:", len(dots))

with open('/home/claude/profile-readme/dots.json', 'w') as f:
    json.dump(dots, f)
