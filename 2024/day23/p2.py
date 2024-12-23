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


def get_connected(fnode):
    nodes = [fnode]
    connected = []
    visit = {}

    while len(nodes) > 0:
        node = nodes.pop(0)
        if node in visit:
            continue
        visit[node] = 1
        add = True
        for n in connected:
            if node not in cons[n]:
                add = False
        if add:
            connected += [node]
            for n in cons[node]:
                nodes += [n]
    return connected
    


best = []
for nn in comp:
    gc = get_connected(nn)
    if len(gc) > len(best):
        best = gc
print(",".join(sorted(best)))
