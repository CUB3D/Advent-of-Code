import functools
import itertools

nums = "789456123 0A"
dirs = " ^A<v>"

def next_key(k, x, y, p):
    i = y * 3 + x
    for direction in p:
        if direction == "<":
            i -= 1
        if direction == ">":
            i += 1
        if direction == "^":
            i -= 3
        if direction == "v":
            i += 3
        yield k[i]

def pathto(k, s, e):
    y1 = k.index(s) // 3
    x1 = k.index(s) % 3
    y2 = k.index(e) // 3
    x2 = k.index(e) % 3

    if x2 > x1:
        h = ">"
    else:
        h = "<"

    if y2 > y1:
        v = "v"
    else:
        v = "^"

    hor = h * abs(x2 - x1)
    ver = v * abs(y2 - y1)

    if ' ' not in next_key(k, x1, y1, hor + ver):
        yield hor + ver + "A"
    if hor + ver != ver + hor:
        if ' ' not in next_key(k, x1, y1, ver + hor):
            yield ver + hor + "A"

@functools.cache
def path_cost(k, s, e, l):
    if l == 0:
        return 1
    mi = 9999999999999
    for path in pathto(k, s, e):
        mi = min(mi, calc(dirs, path, l - 1))
    return mi

@functools.cache
def calc(kp, k, l):
    tmp = 0
    for a, b in itertools.pairwise("A" + k):
        tmp += path_cost(kp, a, b, l)
    return tmp

codes = open("input").read().splitlines()

total = 0
for c in codes:
    total += calc(nums, c, 25 + 1) * int(c[:-1])
print(total)