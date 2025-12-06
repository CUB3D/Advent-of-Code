import functools
import operator
import re
inpu = [re.split("\s+", x.strip()) for x in open("input").readlines()]
cols = list(zip(*inpu))

def calc(c):
    match c[-1]:
        case '*':
            op = operator.mul
            start = 1
        case '+':
            op = operator.add
            start = 0

    return functools.reduce(op, [int(x) for x in c[:-1]], start)

print(sum([calc(c) for c in cols]))



            

