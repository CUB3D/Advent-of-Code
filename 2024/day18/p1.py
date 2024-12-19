inp = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

TEST = False

if not TEST:
    inp = open("input").read().rstrip("\n")


if TEST:
    lim = 12
else:
    lim = 1024

cords = []

for l in inp.split("\n"):
    x = int(l.split(",")[0])
    y = int(l.split(",")[1])
    cords += [(x, y)]


if TEST:
    W = 7
    H = 7
else:
    W = 71
    H = 71

m = [[0 for x in range(W)] for x in range(H)]

for c in cords[:lim]:
    x,y = c
    m[y][x] = 1


spos = (0, 0)
if TEST:
    epos = (5, 5)
else:
    epos = (70, 70)

routes = [(spos, 0)]
seen = []

best = 9999999

c = "\n".join(["".join([str(x) for x in r]) for r in m])
print(c)

while len(routes) > 0:
    (p, s) = routes.pop(0)

    if p == epos:
        if s < best:
            best = s
            print(best)
            continue
    
    if p in seen:
        continue
    seen += [p]
    x,y=p
    
    if y < H -1 and m[y+1][x] == 0:
        routes += [((x, y+1), s+1)]
    if y > 0 and m[y-1][x] == 0:
        routes += [((x, y-1), s+1)]
    if x > 0 and m[y][x-1] == 0:
        routes += [((x-1, y), s+1)]
    if x < W - 1 and m[y][x+1] == 0:
        routes += [((x+1, y), s+1)]

print(best)
