inp = "0 1 10 99 999"

inp = "125 17"

inp = "0 44 175060 3442 593 54398 9 8101095"

inp = [int(x) for x in inp.split(" ")]
#print(" ".join([str(x) for x in inp]))



import math
from functools import cache

p1 = 25
p2 = 75

@cache
def do(n, c):
    if n ==0: return 1

    if c == 0:
        return do(n-1, 1)
    else:
        l = (math.floor(math.log10(c))+1)            
        if l %2 == 0:
            a = c // (10 ** (l>>1))
            b = c % (10 ** (l>>1))
            return do(n-1, a) + do(n-1, b)
        else:
            return do(n-1, c*2024)

ans1 = 0
for c in inp:
    ans1 += do(p1, c)

ans2 = 0
for c in inp:
    ans2 += do(p2, c)
print(ans1, ans2)


# 0.12s for p1 + p2
