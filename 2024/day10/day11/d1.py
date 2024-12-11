inp = "0 1 10 99 999"

inp = "125 17"

inp = "0 44 175060 3442 593 54398 9 8101095"

inp = [int(x) for x in inp.split(" ")]
print(" ".join([str(x) for x in inp]))



v1 = list(inp)
out = []

for jj in range(25):
    for c in v1:
        if c == 0:
            out += [1]
        elif len(str(c)) %2 == 0:
            p = str(c)
            a = p[:len(p)//2]
            b = p[len(p)//2:]
            out += [int(a), int(b)]
        else:
            out += [c*2024]
    #print(" ".join([str(x) for x in out]))
    v1 = list(out)
    out = []

print(len(v1))
        
