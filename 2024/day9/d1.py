inp = "12345"
inp = "2333133121414131402"
inp = open("input").read().split("\n")[0]

exp = []
idx = 0
flg = True
for c in inp:
    if flg:
        exp += [str(idx) for x in range(int(c))]
        idx += 1
    else:
        exp += ["." for x in range(int(c))]
    flg = not flg

print(exp)

lst = len(exp)
while True:
    if lst == 1:
        break

    lst -= 1
    if exp[lst] == '.': continue
    l = lst
    fr = exp.index('.')
    if fr > lst:
        break

    exp[fr],exp[l] = exp[l],'.'

chk = 0
idx = 0
for c in exp:
    if c =='.': continue
    chk += idx*int(c)
    idx += 1
    
print(''.join(exp))
print(chk)

