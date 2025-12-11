inpu = open("input").readlines()
inpu = [x.split(": ") for x in inpu]
inpu = [(x[0], set(x[1].strip().split(" "))) for x in inpu]

d = {}
for (n, c) in inpu:
    d[n] = c
inpu = d

def s(r):
    if r == "out":
        return 1

    t = 0
    for c in inpu[r]:
        t += s(c)
    return t 
    

print(s("you"))
