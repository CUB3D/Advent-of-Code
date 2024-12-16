_inp = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""


_inp = """##########
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

inp = open("input").read().rstrip("\n")

mm = inp.split("\n\n")[0]
ins = inp.split("\n\n")[1]

m = []


for l in mm.split("\n"):
        m += [list(l)]

H = len(m)
W = len(m[0])

ins = list(ins)

for x in range(W):
    for y in range(H):
        if m[y][x] == '@':
            pos = (y, x)
            break

print(pos)

#c = "\n".join(["".join(r) for r in m])
#print(c)

def psh(y, x, ofy, ofx, scale=2):
    if m[y+ofy*scale][x+ofx*scale] == 'O':
        if psh(y, x, ofy, ofx, scale+1):
            m[y+ofy*scale][x+ofx*scale] = 'O'
            m[y+ofy*(scale-1)][x+ofx*(scale - 1)] = '.'
            return True
        else:
            return False
            
    elif m[y+ofy*scale][x+ofx*scale] == '#':
        return False
    elif m[y+ofy*scale][x+ofx*scale] == '.':
        m[y+ofy*scale][x+ofx*scale] = 'O'
        m[y+ofy*(scale-1)][x+ofx*(scale - 1)] = '.'
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
    elif m[y+ofy][x+ofx] == 'O':
        if psh(y, x, ofy, ofx):
            m[pos[0]][pos[1]] = '.'
            pos = (y+ofy, x+ofx) 
            m[pos[0]][pos[1]] = '@'
        
    
    c = "\n".join(["".join(r) for r in m])
    print(c)



ans = 0
for x in range(W):
    for y in range(H):
        if m[y][x] == 'O':
            ans += 100*y + x

print(ans)
