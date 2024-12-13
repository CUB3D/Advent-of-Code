inp = """AAAA
BBCD
BBCC
EEEC"""

inp = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

inp = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

inp = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

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

options = sorted(list(set(inp.replace("\n", ""))))

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
    return out
            
W = len(inp[0])
H = len(inp)

def k(y, x, o, g):
    k = []
    for yy in range(2):
        r = []
        for xx in range(2):
            x1 = x + xx - 1
            y1 = y + yy - 1
            if x1 < 0 or x1 >= W or y1 < 0 or y1 >= H:
                r += [0]
            elif inp[y1][x1] == o and (y1, x1) in g: 
                r += [1]
            else:
                 r += [0]
        k += [r]
    return k

def co(k):
    if k == [[0, 0], [0, 1]]: return 1
    elif k == [[0, 0], [1, 1]]: return 0
    elif k == [[0, 0], [1, 0]]: return 1
    elif k == [[0, 1], [0, 0]]: return 1
    elif k == [[1, 1], [0, 0]]: return 0
    elif k == [[1, 0], [0, 0]]: return 1
    elif k == [[0, 1], [0, 1]]: return 0
    elif k == [[1, 1], [1, 1]]: return 0
    elif k == [[1, 0], [1, 0]]: return 0

    elif k == [[1, 0], [1, 1]]: return 1
    elif k == [[1, 1], [0, 1]]: return 1
    elif k == [[1, 1], [1, 0]]: return 1
    elif k == [[0, 1], [1, 1]]: return 1

    elif k == [[1, 0], [0, 1]]: return 2
    elif k == [[0, 1], [1, 0]]: return 2
    else: 
        print(k)
        print("Unk")
        exit()
            
            
            
            
        
ans = 0
for o in options:
    for y in range(W):
        for x in range(H):
            if (y,x) in sen: continue
            out = ff(y, x, o)
            if len(out) > 0:
                edj = 0
                
                for y1 in range(H+1):
                    for x1 in range(W+1):
                        if (y1, x1) in out or  (y1-1, x1) in out or (y1, x1-1) in out or (y1-1, x1-1) in out:
                            l = k(y1, x1, o, out)
                            c = co(l)
                            edj += c

                perim = 0
                for cy,cx in out:
                    if cx+1 >= W or inp[cy][cx+1] != o:
                        perim +=1
                    if cx == 0 or inp[cy][cx-1] != o:
                        perim +=1
                    if cy+1 >= H or inp[cy+1][cx] != o: perim +=1;
                    if cy == 0 or inp[cy-1][cx] != o: perim +=1;
                ans += edj * len(out)

print(ans) 

