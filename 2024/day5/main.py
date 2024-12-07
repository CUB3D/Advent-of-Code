inp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n")

inp = open("input").readlines()

rules = []
pgs = []
p2 = False
for l in inp:
    l = l.strip()
    if len(l) == 0:
        p2 = True
        continue
    if p2: 
       pgs += [list([int(x) for x in l.split(",")])]  
    else:
        p = l.split("|")
        p0 = int(p[0])
        p1 = int(p[1])
        rules += [(p0,p1)]
    

ans = 0

bad = []

def good(p):
    flg2 = True
    for idx,e in enumerate(p):
        relrule = [(rb,ra) for rb,ra in rules if ra==e and rb in p]
        if relrule:
            if not all([any([e2 == rb for e2 in p[:idx]]) for rb,ra in relrule]):
                flg2 = False
    return flg2

for p in pgs:
    flg2 = good(p)

    if flg2:
        m = p[len(p)//2]
        ans += m
    else:
        bad += [p]

print(ans)

ans2=0
for idx,p in enumerate(bad):
    tmp = [p[0]]
    for x in p[1:]:
        for xi in range(len(tmp)+1):
            tmp1 = list(tmp[::])
            tmp1.insert(xi, x)
            if good(tmp1):
                tmp = tmp1
                break
    m = tmp[len(tmp)//2]
    ans2 += m


print(ans2)
