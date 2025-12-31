inpu = [x.strip() for x in open("input").readlines()]
brk = inpu.index("")
rngs = [x.split("-") for x in inpu[:brk]]
rngs = [(int(x[0]), int(x[1])+1) for x in rngs]
rngs = list(sorted(rngs, key=lambda x: x[0]))
rset = [range(rngs[0][0], rngs[0][1])]
for (rs, re) in rngs[1:]:
    if rs in rset[-1]:
        if re not in rset[-1]:
            rset[-1] = range(rset[-1][0], re)
    else:
        rset += [range(rs, re)]
        

print(sum([len(x) for x in rset]))

