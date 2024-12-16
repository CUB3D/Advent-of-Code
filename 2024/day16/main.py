inp = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

inp = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

_inp = """########
#S...###
####.###
#E...###
########
########"""

inp = open("input").read().rstrip("\n")


m = []
for l in inp.split("\n"):
        m += [list(l)]

H = len(m)
W = len(m[0])


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for x in range(W):
    for y in range(H):
        if m[y][x] == 'S':
            spos = (x, y)
        if m[y][x] == 'E':
            epos = (x, y)
print(spos, epos)

visit = {}
pths = []
routes = [(spos, 0, 0, [])]
best = 10000000000

while len(routes) > 0:
    # why is this 0 like 1000+x faster under pypy?????/
    (p, d, s, cp) = routes.pop(0)

    if p == epos:
        if s < best:
            best = s
            pths = cp+[p]
            pths = list(set(pths))
            #print("NB:", best, len(pths))
            continue
        elif s == best:
            pths += cp
            pths = list(set(pths))
            #print("  NP:", best, len(pths))
    
    if (p, d) in visit:
        if visit[(p,d)] < s:
            continue
    visit[(p, d)] = s
    x,y=p
    
    prevd = d-1
    if prevd < 0:
        prevd += 4

    routes += [((x,y), (d+1)%4, s+1000, cp)]
    routes += [((x,y), prevd, s+1000, cp)]

    ofx,ofy = dirs[d]
    if m[y+ofy][x+ofx] != '#':
        routes += [((x+ofx, y+ofy), d, s+1, cp+[p])]
    
print(best)
print(len(pths))
