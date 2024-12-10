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

inp = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

inp = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

inp = """012345
123456
234567
345678
4.6789
56789."""

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

W = len(inp[0])
h = len(inp)
print(W, h)

ans = 0
v = []
ways = []

def s(tx, ty,w ):
    global ans
    global v
    global ways

    w += [(tx, ty)]



    c = inp[ty][tx]

    if c == '9':
        ways += [w]
        if (ty, tx) in v:
            return 0
        v += [(ty, tx)]
        return 1
    
    if tx+1 < W and inp[ty][tx + 1] == str(int(c)+1):
        s(tx+1, ty, list(w))
    if tx > 0 and inp[ty][tx - 1] == str(int(c)+1):
        s(tx-1, ty, list(w))
    if ty +1 < h and inp[ty+1][tx] == str(int(c)+1):
        s(tx, ty+1, list(w))
    if ty > 0 and inp[ty-1][tx] == str(int(c)+1):
        s(tx, ty-1, list(w))

    return 0

for tx,ty in th:
    v = []
    ways = []
    s(tx, ty, [])
    ans += len(ways)
    print(len(ways))
        
print(ans)
