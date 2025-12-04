inpu = open("input").readlines()

total = 0
for inp in inpu:
    p = [int(x.strip()) for x in inp.strip()]

    first = max(p[:len(p)-1])
    firstpos = p.index(first)
    n = max(p[firstpos+1:])

    nn = first * 10 + n
    total += nn

    print(first, n)
print(total)

