inpu = open("input").readlines()

total = 0
for inp in inpu:
    p = [int(x.strip()) for x in inp.strip()]
    
    x = [0 for _ in range(12)]
    pos = [0 for _ in range(12)]

    x[0] = max(p[:-11])
    pos[0] = p.index(x[0])
    p[pos[0]] = 0
#    print("p", p)
#    print("w", p[pos[0]+1:][:-10])
#    print("X", x)

    for i in range(1, 11):
        x[i] = max(p[pos[i-1]+1:][:-11 + i])
        pos[i] = pos[i-1]+1+p[pos[i-1]+1:].index(x[i])
        p[pos[i]] = 0
#        print("p", p)
#        print("w", p[pos[i-1]+1:][:-11+i])
#        print("X", x)
    x[-1] = max(p[pos[-2]+1:])
    
    total += int("".join([str(x) for x in x]))

  #  print(x, pos)

print(total)

