from itertools import batched
inp = open("input").readlines()[0]

p = inp.split(",")
r = [x.split("-") for x in p]
r = [range(int(x[0]), int(x[1])+1) for x in r]

day1 = 0
for ra in r:
    for d in ra:
        dd = str(d)

        for n in range(2, len(dd)+1):
            if len(set(batched(dd, len(dd)//n))) == 1:
                day1 += d
                break

print(day1)
