inpu = [x.strip() for x in open("input").readlines()]
brk = inpu.index("")
rngs = [x.split("-") for x in inpu[:brk]]
rngs = [range(int(x[0]), int(x[1])+1) for x in rngs]
ing = [int(x) for x in inpu[brk+1:]]
fresh = list(filter(lambda x: any([x in y for y in rngs]), ing))
print(len(fresh))

