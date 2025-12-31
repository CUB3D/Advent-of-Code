import functools
import operator

inpu = [x for x in open("input").readlines()]

nums = ["".join(x) for x in zip(*inpu)]

tmp2 = []
tmp = 0
op = operator.add
for num in nums:
    if len(num.strip()) == 0:
        tmp2 += [tmp]
        continue

    n = int(num[:-1])
    tmp = op(tmp, n)
    if num[-1] == '*':
        tmp = n
        op = operator.mul
    elif num[-1] == '+':
        tmp = n
        op = operator.add
        
print(sum(tmp2))
