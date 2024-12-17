inp = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

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


#C = 9
#prog = [2, 6]
#A = 10
#prog = [5, 0, 5, 1, 5, 4]
#A = 2024
#prog = [0,1,5,4,3,0]
#B = 29
#prog = [1,7]
#B = 2024
#C = 43690
#prog = [4, 0]

def comb(o):
    if o >= 0 and o <= 3:
        return o
    if o == 4:
        return A
    if o == 5:
        return B
    if o == 6:
        return C
    if o == 7:
        print("ASAFASDF")
        exit()


print(A, B, C)
print(prog)

pc = 0
out = []

while True:
    if pc >= len(prog):
        break
    op = prog[pc]
    arg = prog[pc+1]
    
    if op == 0:
        A = int(float(A) / float((2**comb(arg))))
    elif op == 1:
        B = B ^ arg
    elif op == 2:
        B = comb(arg) % 8
    elif op == 3:
        if A != 0:
            pc = arg
            continue
    elif op == 4:
        B = B ^ C
    elif op == 5:
        out += [comb(arg) % 8]
    elif op == 6:
        B = int(float(A) / float((2**comb(arg))))
    elif op == 7:
        C = int(float(A) / float((2**comb(arg))))
    
    pc += 2




print(A, B, C)
print(",".join([str(x) for x in out]))

