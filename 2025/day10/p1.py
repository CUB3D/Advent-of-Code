import itertools

inpu = open("input").readlines()

inp = []

for l in inpu:
    l = l.strip()
    x0 = l.index(']')
    tmp = l[:x0][1:]
    lights = [x == '#' for x in tmp]

    end = l.index('{')
    tmp = l[:end][x0+1:]
    btn = []
    while len(tmp) > 1:
        end2 = tmp.index('(')
        end3 = tmp.index(')')
        tmp1 = tmp[:end3][end2+1:]
        btn += [list([int(x) for x in tmp1.split(",")])]
        
        tmp = tmp[end3+2:]
    inp += [(lights, btn)]
    
total = 0
for (lite, btn) in inp:
    least = 99
    for m in itertools.product([0,1], repeat=len(btn)):
        state = [False]*len(lite)
        for idx in range(len(btn)):
            if m[idx] == 1:
                for l in btn[idx]:
                    state[l] = not state[l]
                if state == lite:
                    least = min(least, sum(m))
    total += least
print(total)
