inp = open("input").read()

shape_sz = []
reg = []
for part in inp.split("\n\n"):
    
    if ":\n" in part:
        sz = sum([int(x == '#') for x in part])
        shape_sz += [sz]
    else:
        for req in part.split("\n"):
            if ": " not in req:
                continue
            tmp = req.split(": ")
            sz = tmp[0]
            sz = list([int(x) for x in sz.split("x")])
            shapes = list([int(x) for x in tmp[1].split(" ")])
            reg += [(sz, shapes)]
        

total = 0
for (sz, cnt) in reg:
    area = sz[0] * sz[1]
    needed_area = 0
    for idx,cou in enumerate(cnt):
        needed_area += cou * shape_sz[idx]
    if needed_area <= area:
        total += 1
print(total)
