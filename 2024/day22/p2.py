
def mix(v, vv):
    return v^vv

def prune(v):
    return v % 16777216
    
def next(v):
    t0 = v * 64
    v = mix(v, t0)
    v = prune(v)
    t0 = v >>5;
    v = mix(v, t0)
    v = prune(v)
    t0 = v*2048
    v= mix(v, t0)
    v = prune(v)
    return v

def next2k(x):
    ret = []
    for _ in range(2000):
        lx = x
        lxp = x%10
        x = next(x)
        ret += [(x, x%10, x%10-lxp)]
    
    #print(ret[:10])
    return ret

inp = [1, 2,3, 2024]

inp = open("input").read().rstrip("\n").split("\n")
inp = [int(x) for x in inp]

pds = []

for p in inp:
    pds += [next2k(p)]


best_price = 0
best_dif = []

lookup = {}
possible_difs = set()

for (idx, pd) in enumerate(pds):
    for i in range(len(pd) - 4 + 1):
        line = pd[i: i + 4]
        difs = list([l[2] for l in line])
        difs_s = str(difs)
        possible_difs.add(difs_s)
        price = line[-1][1]
        k = (idx, difs_s)
        if k not in lookup:
            lookup[k] = price

for difs in possible_difs:
    s = 0
    for idx1 in range(len(pds)):
        k = (idx1, difs)
        if k in lookup:
            s += lookup[k]
    if s > best_price:
        best_price = s
        best_dif = difs
        print("BD", best_dif, best_price)
    
