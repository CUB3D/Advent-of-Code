inp = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

inp = open("input").read()

grd = list([list(i) for i in inp.split('\n')])
print(grd)

def s(y, x):
    global grd

    ans = 0
    ndl = "MAS"

    a = False

    try:
       if x-1 >= 0 and y-1 >= 0 and grd[y-1][x-1] == ndl[0] and grd[y][x] == ndl[1] and grd[y+1][x+1] == ndl[2]: a = True
    except: pass
    try:
       if x-1 >= 0 and y-1 >= 0 and grd[y+1][x+1] == ndl[0] and grd[y][x] == ndl[1] and grd[y-1][x-1] == ndl[2]: a = True
    except: pass

    b = False
    try:
       if x-1 >= 0 and y-1 >= 0 and grd[y+1][x-1] == ndl[0] and grd[y][x] == ndl[1] and grd[y-1][x+1] == ndl[2]: b = True
    except: pass
    try:
       if x-1 >= 0 and y-1 >= 0 and grd[y-1][x+1] == ndl[0] and grd[y][x] == ndl[1] and grd[y+1][x-1] == ndl[2]: b = True
    except: pass


    return a and b

ans = 0
for y in range(len(grd)):
    for x in range(len(grd[y])):
        if s(y, x):
            ans += 1;    

print(ans)
