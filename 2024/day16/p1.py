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
routes = [(spos, 0, 0)]
best = 10000000000

while len(routes) > 0:
    (p, d, score) = routes.pop()

    if p == epos:
        if score < best:
            best = score
            print("NB:", best)
            continue
    
    if (p, d) in visit:
        if visit[(p,d)] < score:
            continue
    visit[(p, d)] = score
    x,y=p
    
    prevd = d-1
    if prevd < 0:
        prevd += 4

    routes += [((x,y), (d+1)%4, score+1000)]
    routes += [((x,y), prevd, score+1000)]

    ofx,ofy = dirs[d]
    if m[y+ofy][x+ofx] != '#':
        routes += [((x+ofx, y+ofy), d, score+1)]
    
print(best)
#print(visit[((1, 13), 0)])
#print(visit[((1, 12), 0)])

    
#def pth(x, y, d, v=[]):
    #print("pth", x, y, d, v, m[y][x])
    #global visit
    #if (v, y, x) in visit:
        #return None

    #visit += [(v, y, x, d)]

#    if m[y][x] == '#':
#        return None
#
#    if m[y][x] == 'E':
#        return v
#

#    ofx,ofy = dirs[d]
#    
#    c = None
#    if m[y][x] == '.' or m[y][x] == 'S':
#        vv = list(v)
#        vv += [(x+ofx, y+ofy)]
#        c =  pth(x+ofx, y+ofy, d, vv)
#    
#    a = pth(x, y, (d+1) % 4, list(v))
#    b = pth(x, y, abs(d-1) % 4, list(v))
#    return [a, b, c]
#

#print(spos, epos)
#x,y = spos
#x = pth(x,y, 0)
#print(x)

