
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

inp = [1, 10, 100, 2024]

inp = open("input").read().rstrip("\n").split("\n")
inp = [int(x) for x in inp]

ans = 0
for ii in inp:
    x = ii
    for _ in range(2000):
        x = next(x)
    ans += x
print(ans)

    
