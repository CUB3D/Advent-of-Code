import math

inpu = open("input").readlines()
inpu = [list([int(x) for x in r.strip().split(",")]) for r in inpu]

d_nodes = {}

for i, n in enumerate(inpu):
    for j, m in enumerate(inpu[i+1:], i+1):
        tmp = math.sqrt(sum((m[k] - n[k]) ** 2 for k in range(3)))
        d_nodes[tmp] = (i, j)


cir = [set([i]) for i in range(len(inpu))]
c_idx = {i: i for i in range(len(inpu))}
cc = len(inpu)


for _, dist in enumerate(sorted(d_nodes.keys())):
    ni, nj = d_nodes[dist]
    ci, cj = c_idx[ni], c_idx[nj]
    if ci != cj:
        cir[ci] = cir[ci].union(cir[cj])
        for n in cir[cj]:
            c_idx[n] = ci
        cir[cj] = set()
        cc -= 1
    if cc == 1:
        print(inpu[ni][0] * inpu[nj][0])
        exit()