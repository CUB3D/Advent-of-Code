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
    for y in opts:
        if a == y:
            return True
        if a[:len(y)] == y:
            if tmp(a[len(y):]):
                return True
    return False
    

ans = 0
for x in rest:
    if tmp(x):
        ans += 1

print(ans)
