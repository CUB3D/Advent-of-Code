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


    def do_dpad(din):
        cpos = (3, 1)
        dout2 = []
        for di in din:
            dout = [[]]
            for elem in di:
                (cpos, x) = dpad_pth(elem, cpos)
                ndin = []
                for d in dout:
                    for pos in x:
                        ndin += [d + pos + ["A"]]
                dout = ndin
            dout2 += dout

        shortest = 999999999
        for l in dout2:
            if len(l) < shortest:
                shortest = len(l)
        filt = list(filter(lambda l: len(l) == shortest, dout2))
        return (shortest, filt)

    (shortest, filt) = do_dpad(din)
    print("dpad0 shortest", shortest)
    (shortest, filt) = do_dpad(filt)
        
    print("dpad1 shortest", shortest)
    num_part = int(code[:3])
    return num_part * shortest

codes = [
"029A",
"980A",
"179A",
"456A",
"379A",
]

codes = open("input").read().rstrip("\n").split("\n")

ans = 0
for c in codes:
    x = p1(c)
    ans += x
print(ans)

