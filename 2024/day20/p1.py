inp = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

inp = open("input").read().rstrip("\n")


m = []
for l in inp.split("\n"):
        m += [list(l)]

H = len(m)
W = len(m[0])


for x in range(W):
    for y in range(H):
        if m[y][x] == 'S':
            spos = (x, y)
        if m[y][x] == 'E':
            epos = (x, y)
print(spos, epos)


visit = {}
routes = [(spos, 0, [])]
best = 10000000000
best_pth = []

while len(routes) > 0:
    (p, s, pth) = routes.pop(0)

    if p == epos:
        if s < best:
            best = s
            best_pth = pth
            continue
    
    if p in visit:
        if visit[p] < s:
            continue
    visit[p] = s
    x,y=p
    
    if m[y+1][x+0] != '#':
        routes += [((x+0, y+1), s+1, pth+[p])]
    if m[y-1][x+0] != '#':
        routes += [((x+0, y-1), s+1, pth+[p])]
    if m[y][x+1] != '#':
        routes += [((x+1, y), s+1, pth+[p])]
    if m[y][x-1] != '#':
        routes += [((x-1, y), s+1, pth+[p])]

best_pth += [epos]
normal_best = best


ans = 0
for (px,py) in best_pth:
    i1 = best_pth.index((px, py))       
    for dx in range(-5, 5):
        for dy in range(-5, 5):
            if dx == 0 and dy == 0:
                continue
            nx=dx+px
            ny=dy+py
            if (nx,ny) in best_pth:
                i2 = best_pth.index((nx, ny))       
                if i2 <= i1:
                    continue
                cd = abs(dx)+abs(dy)
                if 1 <= cd <= 2:
                    ct = i1+cd
                    if i2 >= ct+100:
                        ans += 1
              

print(ans)
