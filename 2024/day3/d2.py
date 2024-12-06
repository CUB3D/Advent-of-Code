#inp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
inp = open("input").read()

def tk(x, v):
    if x[:len(v)] == v:
        return x[len(v):]
    return False

def dig(x):
    i  = 1
    while x[:i].isdigit():
        i+=1
    i-=1
    return (x[i:], int(x[:i]))

inp_ = "a" + inp
ans = 0
en = True
while True:
    inp_ = inp_[1:]
    if len(inp_) < 7:
        break
    inp2 = tk(inp_, "do()")
    if inp2:
        en = True
        inp = inp2
        continue
    
    inp2 = tk(inp_, "don't()")
    if inp2:
        en = False
        inp = inp2
        continue
        

    inp = tk(inp_, "mul(")
    if not inp:
        continue
    (inp, a) = dig(inp)    
    if not inp:
        continue
    inp = tk(inp, ",")
    if not inp:
        continue
    (inp, b) = dig(inp)    
    if not inp:
        continue
    inp = tk(inp, ")")
    if not inp:
        continue
    print(a, b)
    if en:
        ans += a*b

        
print("D3p1",ans)
