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
idx -= 1
while idx > 0:
    st = exp.index(str(idx))
    en = 0
    try:
        en = st
        while exp[en] == str(idx):
            en += 1
    except: pass

    ops = 0 
    nsz = (en-st)
    ndl = ["."] * nsz
    for x in range(st + 2):
        if x > st or len(exp[x:x+nsz]) < nsz:
            ops = -1
            break
        if exp[x:x+nsz] == ndl:
            ops = x
            break
    if ops != -1 and ops < st:
        for i in range(nsz):
            exp[x+i] = exp[st+i]
            exp[st+i] = '.'

    idx -= 1

chk = 0
idx = 0
for idx,c in enumerate(exp):
    if c =='.': continue
    chk += idx*int(c)
    
print(''.join(exp))
print(chk)

