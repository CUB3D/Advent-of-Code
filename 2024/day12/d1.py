inp = """AAAA
BBCD
BBCC
EEEC"""

inp = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""


inp = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

inp = open("input").read()[:-1]

options = set(inp.replace("\n", ""))

inp = inp.split("\n")


sen = []

def ff(y,x, o):
    global sen

    out = []
    s = []
    v = [(y, x)]
    while len(v) > 0:
        vy,vx = v.pop()
        if H <= vy or vy < 0 or W <= vx or vx < 0: continue
        if (vy,vx) in s: continue
        s += [(vy,vx)]
        if inp[vy][vx] == o:
            out += [(vy, vx)]
            v += [(vy+1,vx), (vy-1,vx), (vy,vx+1), (vy,vx-1)]
    sen += out
    sen = list(set(sen))
    #print(o, out)
    return out
            
W = len(inp[0])
H = len(inp)
        
ans = 0
for o in options:
    for y in range(W):
        for x in range(H):
            if (y,x) in sen: continue
            #print("chk", sen, y, x)
            out = ff(y, x, o)
            if len(out) > 0:
                #print(sen, y, x)
                print("Area", o, len(out), out)

                perim = 0
                for cy,cx in out:
                    if cx+1 >= W or inp[cy][cx+1] != o: perim +=1
                    if cx == 0 or inp[cy][cx-1] != o: perim +=1
                    if cy+1 >= H or inp[cy+1][cx] != o: perim +=1
                    if cy == 0 or inp[cy-1][cx] != o: perim +=1
                print("per", perim)
                ans += perim * len(out)

print(ans) 
