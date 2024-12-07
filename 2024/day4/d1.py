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

def s(ndl, y, x):
    global grd

    ans = 0
    try:
        if grd[y][x] == ndl[0] and grd[y][x+1] == ndl[1] and grd[y][x+2] == ndl[2] and grd[y][x+3] == ndl[3]: ans += 1;print(x,y)#grd[y][x] = '.';grd[y][x+1] = '.';grd[y][x+2] = '.';grd[y][x+3] = '.'
    except: pass
    try:
        if x-3>=0 and grd[y][x] == ndl[0] and grd[y][x-1] == ndl[1] and grd[y][x-2] == ndl[2] and grd[y][x-3] == ndl[3]: ans += 1;print(x,y)#grd[y][x] = '.';grd[y][x+1] = '.';grd[y][x+2] = '.';grd[y][x+3] = '.'
    except: pass

    try:
        if grd[y][x] == ndl[0] and grd[y+1][x] == ndl[1] and grd[y+2][x] == ndl[2] and grd[y+3][x] == ndl[3]: ans += 1;print(x,y)#grd[y][x] = '.';grd[y+1][x] = '.';grd[y+2][x] = '.';grd[y+3][x] = '.'
    except: pass
    try:
        if y-3 >= 0 and grd[y][x] == ndl[0] and grd[y-1][x] == ndl[1] and grd[y-2][x] == ndl[2] and grd[y-3][x] == ndl[3]: ans += 1;
    except: pass

    try:
       if grd[y][x] == ndl[0] and grd[y+1][x+1] == ndl[1] and grd[y+2][x+2] == ndl[2] and grd[y+3][x+3] == ndl[3]: ans += 1
    except: pass
    try:
       if x-3 >= 0 and y-3 >= 0 and grd[y][x] == ndl[0] and grd[y-1][x-1] == ndl[1] and grd[y-2][x-2] == ndl[2] and grd[y-3][x-3] == ndl[3]: ans += 1
    except: pass

    try:
       if x-3 >=0 and grd[y][x] == ndl[0] and grd[y+1][x-1] == ndl[1] and grd[y+2][x-2] == ndl[2] and grd[y+3][x-3] == ndl[3]: ans += 1
    except: pass
    try:
       if y-3 >=0 and grd[y][x] == ndl[0] and grd[y-1][x+1] == ndl[1] and grd[y-2][x+2] == ndl[2] and grd[y-3][x+3] == ndl[3]: ans += 1
    except: pass

    return ans

ans = 0
for y in range(len(grd)):
    for x in range(len(grd[y])):
        ndl = "XMAS"
        ans += s(ndl, y, x)

print(ans)
