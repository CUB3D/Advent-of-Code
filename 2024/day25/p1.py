inp = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

inp = open("input").read().rstrip("\n")

parts = inp.split("\n\n")

locks = []
keys = []

for sec in parts:
    lines = sec.split("\n")
    pins = [0, 0, 0, 0, 0] 
    if lines[0] == "#####":
        for r in lines[1:]:
            for (idx, c) in enumerate(r):
                if c == '#':
                    pins[idx] += 1
        locks += [pins]
    else:
        for r in lines[:-1]:
            for (idx, c) in enumerate(r):
                if c == '#':
                    pins[idx] += 1
        keys += [pins]


print(locks)
print(keys)

ans = 0

for l in locks:
    for k in keys:
        flag = True
        for idx in range(len(l)):
            if l[idx] + k[idx] > 5:
                flag = False
        if flag:
            ans += 1
        
print(ans)
