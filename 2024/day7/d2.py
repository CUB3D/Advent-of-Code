inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")

inp = open("input").readlines()

import math

eqs = []

for l in inp:
    ans = int(l.split(": ")[0])
    args = [int(x) for x in l.split(": ")[1].split(" ")]
    eqs += [(ans, args)]
print(eqs)

ans = 0

for eq in eqs:
    print(eq)
    for b in range(0, 1<<22):
        tmp = eq[1][0]
        for idx,n in enumerate(eq[1][1:]):
            if b & (0b11<<(idx*2)) == (0b00<<(idx*2)):
                tmp = tmp * 10**(int(math.log10(n))+1) + n
            elif b & (0b11<<(idx*2)) == (0b01<<(idx*2)):
                tmp *= n
            else:
                tmp += n
        if tmp == eq[0]:
          ans += tmp  
          break
print(ans)


