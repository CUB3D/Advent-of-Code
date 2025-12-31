import itertools
import z3

inpu = open("input").readlines()

inp = []

for l in inpu:
    l = l.strip()
    x0 = l.index(']')
    tmp = l[:x0][1:]
    lights = [x == '#' for x in tmp]

    end = l.index('{')
    tmp = l[:end][x0+1:]
    btn = []
    while len(tmp) > 1:
        end2 = tmp.index('(')
        end3 = tmp.index(')')
        tmp1 = tmp[:end3][end2+1:]
        btn += [list([int(x) for x in tmp1.split(",")])]
        
        tmp = tmp[end3+2:]

    tmp = l[end+1:][:-1]
    exp = list([int(x) for x in tmp.split(",")])

    inp += [(lights, btn, exp)]
    
def solve(lite, btn, exp, minvl):
    s = z3.Solver()

    vs = []
    for i in range(len(btn)):
        vs += [z3.Int("x"+str(i))]
        s.add(vs[-1] >= 0)
    
    if minvl is not None:
        minb = 0
        for v in vs:
            minb += v
        s.add(minb < minvl) 

    for li in range(len(lite)):
        eq = 0
        haseq = False
        for idx,bt in enumerate(btn):
            if li in bt:
                eq += vs[idx]   
                haseq=True
        if haseq:
            s.add(eq == exp[li])

    s.check()
    try:
        res = s.model()
        su = 0
        for b in vs:
            su += res[b].as_long()
        return su
    except:
        return None

total = 0
for (lite, btn, exp) in inp:
    minv = None
    while True:
        nv = solve(lite, btn, exp, minv)
        if nv is not None:
            if minv is None or nv < minv:
                minv = nv
        else:
            break
    total += minv

print(total)
    
        
