inp = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

TEST = False

if not TEST:
    inp = open("input").read()[:-1]

r = []

inp = inp.split("\n")

for l in inp:
    p = l.split(" ")
    po = p[0][2:]
    v = p[1][2:]
    
    px = int(po.split(",")[0])
    py = int(po.split(",")[1])

    vx = int(v.split(",")[0])
    vy = int(v.split(",")[1])

    r += [[(px, py), (vx, vy)]]

W = 11
H = 7

if not TEST:
    W = 101
    H = 103



world = list([[' ' for x in range(W)] for x in range(H)])
for _ in range(10000):
    for x in range(W):
        for y in range(H):
            world[y][x] = ' '
    for idx in range(len(r)):

        px,py = r[idx][0]
        vx,vy = r[idx][1]
        nx,ny = (px+vx, py+vy)
        if nx < 0: nx = W + nx
        nx = nx % W
        if ny < 0: ny = H + ny
        ny = ny % H
        r[idx] = [(nx, ny), (vx, vy)]

        world[ny][nx] = '#'

    c = "\n".join(["".join(r) for r in world])
    if "########" in c:
        print(c)
        print(_+1)
        exit()

