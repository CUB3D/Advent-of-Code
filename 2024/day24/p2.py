inp = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

inp = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

inp = open("input").read().rstrip("\n")

pt = inp.split("\n\n")


wires = {}
for l in pt[0].split("\n"):
    el = l.split(": ")
    wires[el[0]] = int(el[1]) 

all_wire = set()
conn = []
for g in pt[1].split("\n"):
    el = g.split(" ")
    a = el[0]
    b = el[2]
    o = el[4]

    all_wire.add(a)
    all_wire.add(b)
    all_wire.add(o)

    if el[1] == "AND":
        conn += [(a, b, "&", o)]
    elif el[1] == "OR":
        conn += [(a, b, "|", o)]
    elif el[1] == "XOR":
        conn += [(a, b, "^", o)]


all_wires2 = set(all_wire)
conn2 = list(conn)
wires2 = dict(wires)

for bit in range(45):
    all_wires = set(all_wires2)
    conn = list(conn2)
    wires = dict(wires2)
    normal_iters = 0

    for x in range(99):
        xx = str(x)
        while len(xx) < 2:
            xx = "0" + xx 
        k = "y"+xx
        if k in wires:
            wires[k] = 0

    for x in range(99):
        xx = str(x)
        while len(xx) < 2:
            xx = "0" + xx 
        k = "x"+xx
        if k in wires:
            wires[k] = 0

    k = str(bit)
    if len(k) < 2:
        k = "0" + k
    wires["x"+k] = 1
    wires["y"+k] = 1

    while len(wires.keys()) < len(all_wire):
        normal_iters += 1
        for (idx, (a, b, m, o)) in enumerate(conn):
            #print(a, m, b, o)
            if a in wires and b in wires:
                a = wires[a]
                b = wires[b]

                cc0,cc1 = ("z14", "vss")
                if o == cc0:
                    o = cc1
                elif o == cc1:
                    o = cc0

                cc0,cc1 = ("kdh", "hjf")
                if o == cc0:
                    o = cc1
                elif o == cc1:
                    o = cc0

                cc0,cc1 = ("z31", "kpp")
                if o == cc0:
                    o = cc1
                elif o == cc1:
                    o = cc0

                cc0,cc1 = ("sgj", "z35")
                if o == cc0:
                    o = cc1
                elif o == cc1:
                    o = cc0

                if m == "&":
                   wires[o] = a & b
                elif m == "|":
                   wires[o] = a | b
                elif m == "^":
                   wires[o] = a ^ b

                #print(o, "=", wires[o])

                del conn[idx]
                continue           
            else:
                pass

    ans = ""
    for x in range(99):
        xx = str(x)
        while len(xx) < 2:
            xx = "0" + xx 
        k = "z"+xx
        if k in wires:
            ans = str(wires[k]) + ans
        
    z = eval("0b" + ans)

    ans = ""
    for x in range(99):
        xx = str(x)
        while len(xx) < 2:
            xx = "0" + xx 
        k = "x"+xx
        if k in wires:
            ans = str(wires[k]) + ans
    xans = eval("0b" + ans)

    ans = ""
    for x in range(99):
        xx = str(x)
        while len(xx) < 2:
            xx = "0" + xx 
        k = "y"+xx
        if k in wires:
            ans = str(wires[k]) + ans
    y = eval("0b" + ans)

    print(xans, "+", y, z)

    if z != xans + y:
        print("bit", bit)


# plot the netlist
import graphviz
dot = graphviz.Digraph(comment='The Round Table')

for w in all_wires:
    dot.node(w, w)

idxi = 0
for (a, b, m, o) in conn2:
    idx = str(idxi)
    dot.node(idx, a+ " " + m + " " + b)
    dot.edge(a, idx)
    dot.edge(b, idx)
    dot.edge(idx, o)
    
    idxi+=1

dot.render('round-table.gv').replace('\\', '/')

# just read the gates lol
print(",".join(sorted(["z14","vss", "kdh", "hjf", "z31", "kpp", "sgj", "z35"])))
