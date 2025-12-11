import functools

inpu = open("input").readlines()
inpu = [x.split(": ") for x in inpu]
inpu = [(x[0], set(x[1].strip().split(" "))) for x in inpu]

d = {}
for (n, c) in inpu:
    d[n] = c
inpu = d

@functools.cache
def s(r, n, f):
    if r == "out":
        return n

    if r == "fft" or r == "dac":
        f += 1

    t = 0
    if f == 2:
        n = 1
    for c in inpu[r]:
        t += s(c, n, f)
    return t 
    

print(s("svr", n=0, f=0))
