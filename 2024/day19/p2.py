inp = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

inp = open("input").read().rstrip("\n")


stp = inp.split("\n\n")

opts = stp[0].split(", ")

rest = stp[1].split("\n")

from functools import cache

@cache
def tmp(a):
    s = 0
    for y in opts:
        if a == y:
            s += 1
        elif a[:len(y)] == y:
            s += tmp(a[len(y):])
    return s
    

ans = 0
for x in rest:
    ans += tmp(x)

print(ans)
