from functools import cache

numpads = """#####
#789#
#456#
#123#
##0A#
#####"""

dpads = """#####
##^A#
#<v>#
#####"""

numpad = []
for l in numpads.split("\n"):
        numpad += [list(l)]

dpad = []
for l in dpads.split("\n"):
        dpad += [list(l)]

def numpad_pth(tgt, spos):
    m = numpad

    H = len(m)
    W = len(m[0])


    for x in range(W):
        for y in range(H):
            if m[y][x] == tgt:
                epos = (x, y)


    visit = {}
    routes = [(spos, 0, [])]
    best = 10000000000
    best_pths = []

    while len(routes) > 0:
        (p, s, pth) = routes.pop(0)

        if p == epos:
            if s < best:
                best = s
                best_pths = [pth]
                continue
            elif s == best:
                best_pths += [pth]
                continue
        
        if p in visit:
            if visit[p] < s:
                continue
        visit[p] = s
        x,y=p
        
        if m[y+1][x+0] != '#':
            routes += [((x+0, y+1), s+1, pth+['v'])]
        if m[y-1][x+0] != '#':
            routes += [((x+0, y-1), s+1, pth+['^'])]
        if m[y][x+1] != '#':
            routes += [((x+1, y), s+1, pth+['>'])]
        if m[y][x-1] != '#':
            routes += [((x-1, y), s+1, pth+['<'])] 
    return (epos, best_pths)

def dpad_pth(tgt, spos):
    m = dpad

    H = len(m)
    W = len(m[0])


    epos = None
    for x in range(W):
        for y in range(H):
            if m[y][x] == tgt:
                epos = (x, y)

    if not epos:
        print("NOT FOUND", tgt)


    visit = {}
    routes = [(spos, 0, [])]
    best = 10000000000
    best_pths = []

    while len(routes) > 0:
        (p, s, pth) = routes.pop(0)

        if p == epos:
            if s < best:
                best = s
                best_pths = [pth]
                continue
            elif s == best:
                best_pths += [pth]
                continue
        
        if p in visit:
            if visit[p] < s:
                continue
        visit[p] = s
        x,y=p
        
        if m[y+1][x+0] != '#':
            routes += [((x+0, y+1), s+1, pth+['v'])]
        if m[y-1][x+0] != '#':
            routes += [((x+0, y-1), s+1, pth+['^'])]
        if m[y][x+1] != '#':
            routes += [((x+1, y), s+1, pth+['>'])]
        if m[y][x-1] != '#':
            routes += [((x-1, y), s+1, pth+['<'])] 
    return (epos, best_pths)

def p1(code):
    cpos = (3,4)
    din = [[]]
    for elem in code:
        (cpos, x) = numpad_pth(elem, cpos)
        ndin = []
        for d in din:
            for pos in x:
                ndin += [d + pos + ["A"]]
        din = ndin

    def base(v, cpos):
        (ig, best_pth) = dpad_pth(v, cpos)
        return (ig, len(best_pth[0]))

    def base1(v, cpos):
        (tpos, best_pths) = dpad_pth(v, cpos)

        short = 99999999
        spath = 0
        for pth in best_pths:
            cost = 0
            tpos1 = (3,1)
            for vv in pth:
                (tpos1,cd) = base(vv, tpos1)
                cost += cd
            (_tpos,cd) = base("A", tpos1)
            cost += cd 
            if cost < short:
                short = cost
                spath = pth
        return (tpos, "".join(spath))

    @cache
    def base2(s, c=1): 
        ttt = 0
        tpos = (3,1)
        for v in s:
            (tpos,cd) = base1(v, tpos)
            if c > 1:
                ttt += base2(cd+"A", c-1) 
            else:        
                cd = len(cd)
                ttt += cd + 1
        return ttt

    shortest = 999999999999999999999
    for cc in din:
        t = base2("".join(cc), c=2)
        if t < shortest:
            shortest = t
    print(shortest)

    num_part = int(code[:3])
    return num_part * shortest

codes = open("input").read().rstrip("\n").split("\n")


ans = 0
for c in codes:
    x = p1(c)
    ans += x
print(ans)

