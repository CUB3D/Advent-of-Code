inp = open("input").readlines()[0]

p = inp.split(",")
r = [x.split("-") for x in p]
r = [range(int(x[0]), int(x[1])+1) for x in r]

day1 = 0
for ra in r:
    for d in ra:
        dd = str(d)
        i = len(dd)//2
        if dd[i:] == dd[:i]:
            day1 += d

print(day1)
