import shapely

inpu = open("input").readlines()
inpu = [x.split(",") for x in inpu]
inpu = [(int(x[0]), int(x[1])) for x in inpu]

poly = shapely.geometry.Polygon(inpu)

big = 0

for (sx, sy) in inpu:
    for (ox, oy) in inpu:
        sz = (abs(sx-ox)+1) * (abs(sy-oy)+1)
        if poly.contains(shapely.geometry.Polygon([(sx, sy), (ox, sy), (ox, oy), (sx, oy)])):
            big = max(sz, big)
print(big)
