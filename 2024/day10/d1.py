inp = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

inp = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

inp = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

inp = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

inp = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

inp = open("input").read()[:-1]

inp = inp.split("\n")


inp = list([list(x) for x in inp])
print(inp)

th = []
for y,r in enumerate(inp):
    for x,c in enumerate(r):
        if c == '0':
            th += [(x, y)]

print(th)

w = len(inp[0])
h = len(inp)
print(w, h)

ans = 0
v = []

def s(tx, ty):
    global ans
    global v
    if (ty, tx) in v:
        return

    v += [(ty, tx)]

    c = inp[ty][tx]

    if c == '9':
        ans += 1
        return

    if tx+1 < w and inp[ty][tx + 1] == str(int(c)+1):
        s(tx+1, ty)
    if tx > 0 and inp[ty][tx - 1] == str(int(c)+1):
        s(tx-1, ty)
    if ty +1 < h and inp[ty+1][tx] == str(int(c)+1):
        s(tx, ty+1)
    if ty > 0 and inp[ty-1][tx] == str(int(c)+1):
        s(tx, ty-1)

for tx,ty in th:
    v = []
    s(tx, ty)
print(ans)
