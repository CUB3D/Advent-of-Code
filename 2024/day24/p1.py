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

while len(wires.keys()) < len(all_wire):
    for (idx, (a, b, m, o)) in enumerate(conn):
        if a in wires and b in wires:
            a = wires[a]
            b = wires[b]

            if m == "&":
               wires[o] = a & b
            elif m == "|":
               wires[o] = a | b
            elif m == "^":
               wires[o] = a ^ b

            print(o, "=", wires[o])

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
    
print(eval("0b" + ans))
