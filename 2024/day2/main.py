inp = open("input").readlines()
ll = [[int(n) for n in l.strip().split(' ')] for l in inp]
incdec = [sorted(l) == l or sorted(l)[::-1] == l for l in ll]
difs = [all([1 <= abs(a-b) <= 3  for a,b in zip(l, l[1:])]) for l in ll]
ans = len(list(filter(None, [a and b for a,b in zip(incdec, difs)])))
print("Day2p1", ans)

cnt = 0 
for idx,lst in enumerate(ll):
    if not (incdec[idx] and difs[idx]):
        for i in range(len(lst)):
            l = list(lst[::])
            del l[i]
            if all([1 <= abs(a-b) <= 3  for a,b in zip(l, l[1:])]) and (sorted(l) == l or sorted(l)[::-1] == l):
                cnt += 1
                break

print(cnt + ans)
