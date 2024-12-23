inp = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

inp = open("input").read().rstrip("\n")


from collections import defaultdict

cons = defaultdict(list)
comp = set()

for l in inp.split("\n"):
    p = l.split("-")
    a = p[0]
    b = p[1]
    comp.add(a)
    comp.add(b)

    cons[a] += [b]
    cons[b] += [a]

def chkn(g):
    for t in g:
        if t[0] == 't':
            return True
    return False
     

grups = set()
for a in comp:
    for b in comp:
        for c in comp:
            if b in cons[a] and c in cons[a] and b in cons[c]:
                grups.add(tuple(sorted([a, b, c])))

ans = 0
for g in grups:
    if chkn(g):
        ans += 1  
print(ans)
