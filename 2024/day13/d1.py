inp = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

inp = open("input").read()

inp = inp.split("\n\n")

import z3

tokens = 0
prize = 0

for s in inp:
    l = s.split("\n")
    #print(l)
    a=l[0].split(" ")[2].replace("X+", "").replace(",", "")
    b=l[0].split(" ")[3].replace("Y+", "").replace(",", "")

    c=l[1].split(" ")[2].replace("X+", "").replace(",", "")
    d=l[1].split(" ")[3].replace("Y+", "").replace(",", "")

    e=l[2].split(" ")[1].split("=")[1].replace(",", "")
    f=l[2].split(" ")[2].split("=")[1].replace(",", "")

    x = z3.Int('x')
    y = z3.Int('y')
    
    e = int(e)
    f = int(f)

    s = z3.Solver()
    s.add(z3.And(e == a*x + c*y, f==b*x + d*y))
    c = s.check()
    if c == z3.unsat:
        continue

    prize += 1
    m = s.model()

    apres = m[x].as_long()
    bpres = m[y].as_long()
    tokens += 3*apres + bpres

print(tokens)

