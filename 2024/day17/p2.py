inp = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

inp = open("input").read().rstrip("\n")

for l in inp.split("\n"):
    if "A:" in l:
        A = int(l.split("A: ")[-1])
    if "B:" in l:
        B = int(l.split("B: ")[-1])
    if "C:" in l:
        C = int(l.split("C: ")[-1])
    if "Program:" in l:
        prog = list([int(x) for x in l.split("Program: ")[-1].split(",")])


def comb(o):
    if o >= 0 and o <= 3:
        return o
    elif o == 4:
        return A
    elif o == 5:
        return B
    elif o == 6:
        return C


print(A, B, C)
print(prog)

pc = 0
out = []

SA = 0
SB = B
SC = C

SA = 0
inc = 1


print(SA)
c = 1
while True:
    pc = 0
    out.clear()
    A = SA
    SA += inc
    B = SB
    C = SC
    

    while True:
        if pc >= len(prog):
            break
        op = prog[pc]
        arg = prog[pc+1]
        
        if op == 0:
            A = A >> comb(arg)
        elif op == 1:
            B = B ^ arg
        elif op == 2:
            B = comb(arg) & 0b111
        elif op == 3:
            if A != 0:
                pc = arg
                continue
        elif op == 4:
            B = B ^ C
        elif op == 5:
            out += [comb(arg) & 0b111]

            if len(out) >= c and prog[:c] == out:
                print(SA-inc)
                print(out)
                print(prog)
                c += 1
                if len(out) == 5:
                    SA = SA - inc
                    inc = 1 << (3*5)
                    continue
                if len(out) == 9:
                    SA = SA - inc
                    inc = 1 << (3*8)
                    continue
            if prog == out:
                print("Ans: ", SA-inc)
                exit()
        elif op == 6:
            B = A >> comb(arg)
        elif op == 7:
            C = A >> comb(arg)
        
        pc += 2





print(A, B, C)
print(",".join([str(x) for x in out]))

