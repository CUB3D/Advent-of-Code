_inp = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""


_np = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

_inp = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

_inp = """#######
#...#.#
#.....#
#..OO.#
#..OO@#
#.....#
#######

<<<<"""

_inp = """#######
#...#.#
#.....#
#...O.#
#...@.#
#.....#
#######

>^"""

_inp = """#######
#...#.#
#.....#
#...O@#
#...O.#
#.....#
#######

<>vvvvv<^"""

_inp = """#######
#.....#
#.....#
#..@O.#
#...O.#
#.....#
#######

>><vvvvv>>^^"""

_inp = """#######
#.....#
#...@.#
#...O.#
#..OO.#
#.....#
#######

>>v<^<v"""

_inp = """#######
#.....#
#...#.#
#..OO.#
#.@O..#
#.....#
#######

>>v>^"""

inp = open("input").read().rstrip("\n")

mm = inp.split("\n\n")[0]
ins = inp.split("\n\n")[1]


m = []


for l in mm.split("\n"):
        r = []
        for c in l:
            if c == '.':
                r += ['.', '.']
            elif c == '#':
                r += ['#', '#']
            elif c == 'O':
                r += ['[', ']']
            elif c == '@':
                r += ['@', '.']
        m += [r]

print(m)

H = len(m)
W = len(m[0])

print(W, H)

ins = list(ins)

for x in range(W):
    for y in range(H):
        if m[y][x] == '@':
            pos = (y, x)
            break

print(pos)

#c = "\n".join(["".join(r) for r in m])
#print(c)

def pshyu(y, x, ofy, ofx, scale, d):
    global m
    #print("pshyu", y, x, ofy, ofx, scale, "D:", d, y+ofy*scale, x+ofx*scale, m[y+ofy*scale][x+ofx*scale])

    if m[y+ofy*(scale+1)][x] == '#' or m[y+ofy*(scale+1)][x+1] == '#':
        return False


    # direct above
    if m[y+ofy*(scale+1)][x] == '[':
        if pshyu(y, x, ofy, ofx, scale+1, d):

            m[y+ofy*(scale+1)][x] = '['
            m[y+ofy*(scale+1)][x+1] = ']'

            m[y+ofy*scale][x] = '.'
            m[y+ofy*scale][x+1] = '.'
            
            return True 
        else:
            return False

    flag = True
    flag2 = False
    map2 = list([list(r) for r in m])

    # left above
    if m[y+ofy*(scale+1)][x] == ']' and flag:
        flag2 = True
        if pshyu(y, x-1, ofy, ofx, scale+1, d):
            
            flag = True
        else:
            flag = False

    # right above
    if m[y+ofy*(scale+1)][x+1] == '[' and flag:
        flag2 = True
        if pshyu(y, x+1, ofy, ofx, scale+1, d):
            m[y+ofy*(scale+1)][x] = '['
            m[y+ofy*(scale+1)][x+1] = ']'

            m[y+ofy*scale][x] = '.'
            m[y+ofy*scale][x+1] = '.'
            
            flag = True
        else:
            flag = False

    if flag2:
        if flag:
            m[y+ofy*(scale+1)][x] = '['
            m[y+ofy*(scale+1)][x+1] = ']'

            m[y+ofy*scale][x] = '.'
            m[y+ofy*scale][x+1] = '.'
        else:
            m = map2
        return flag

    if m[y+ofy*(scale+1)][x] == '.' and m[y+ofy*(scale+1)][x+1] == '.':
        m[y+ofy*(scale+1)][x] = '['
        m[y+ofy*(scale+1)][x+1] = ']'

        m[y+ofy*scale][x] = '.'
        m[y+ofy*scale][x+1] = '.'

        return True
    

def pshx(y, x, ofy, ofx, scale, d=0):
    #print("pshx", y, x, ofy, ofx, scale, "D:", d, y+ofy*scale, x+ofx*scale, m[y+ofy*scale][x+ofx*scale])
    if (d == 0 and m[y+ofy*scale][x+ofx*(scale+2)] == ']') or (d == 1 and m[y+ofy*scale][x+ofx*(scale+2)] == '['):
        if pshx(y, x, ofy, ofx, scale+2, d):
            if d == 0:
                m[y+ofy*scale][x+ofx*(scale+2)] = '['
                m[y+ofy*scale][x+ofx*(scale+1)] = ']'
            else:
                m[y+ofy*scale][x+ofx*(scale+2)] = ']'
                m[y+ofy*scale][x+ofx*(scale+1)] = '['

            m[y+ofy*(scale-1)][x+ofx*(scale - 1)] = '.'
            return True
        else:
            return False
            
    elif m[y+ofy*scale][x+ofx*scale] == '#':
        return False
    elif m[y+ofy*scale][x+ofx*(scale+2)] == '.':
        if d == 0:
            m[y+ofy*scale][x+ofx*(scale+1)] = ']'
            m[y+ofy*scale][x+ofx*(scale+2)] = '['
        else:
            m[y+ofy*scale][x+ofx*(scale+1)] = '['
            m[y+ofy*scale][x+ofx*(scale+2)] = ']'

        m[y+ofy*(scale-1)][x+ofx*(scale-1)] = '.'
        return True
    
    

for ci in ins:
    if ci == '\n': continue
    y,x = pos
    if ci == '<':
        ofx,ofy = (-1, 0)
    elif ci == '^':
        ofx,ofy = (0, -1)
    elif ci == '>':
        ofx,ofy = (1, 0)
    elif ci == 'v':
        ofx,ofy = (0, 1)
    
    if m[y+ofy][x+ofx] == '#':
        pass
    elif m[y+ofy][x+ofx] == '.':
        m[pos[0]][pos[1]] = '.'
        pos = (y+ofy, x+ofx) 
        m[pos[0]][pos[1]] = '@'
    elif ofx != 0 and m[y+ofy][x+ofx] == ']':
        if pshx(y, x, ofy, ofx, scale=1, d=0):
            m[pos[0]][pos[1]] = '.'
            pos = (y+ofy, x+ofx) 
            m[pos[0]][pos[1]] = '@'
    elif ofx != 0 and m[y+ofy][x+ofx] == '[':
        if pshx(y, x, ofy, ofx, scale=1, d=1):
            m[pos[0]][pos[1]] = '.'
            pos = (y+ofy, x+ofx) 
            m[pos[0]][pos[1]] = '@'
    elif ofy !=0 and m[y+ofy][x+ofx] == '[':
        if pshyu(y, x, ofy, ofx, scale=1, d=0):
            m[pos[0]][pos[1]] = '.'
            pos = (y+ofy, x+ofx) 
            m[pos[0]][pos[1]] = '@'
    elif ofy != 0 and m[y+ofy][x+ofx] == ']':
        if pshyu(y, x-1, ofy, ofx, scale=1, d=0):
            m[pos[0]][pos[1]] = '.'
            pos = (y+ofy, x+ofx) 
            m[pos[0]][pos[1]] = '@'
    
    #c = "\n".join(["".join(r) for r in m])
    #print(c)
    #if ".]" in c or "[." in c or "]]" in c or "[[" in c or "@]" in c or "[@" in c: 
    #    exit()



ans = 0
for x in range(W):
    for y in range(H):
        if m[y][x] == '[':
            ans += 100*y + x

print(ans)

