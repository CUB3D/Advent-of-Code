inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

inp = open("input").read()

inp = inp.split("\n")


pos = (0,0)
for y,r in enumerate(inp):
    for x,c in enumerate(r):
        if c == '^': pos = (x, y)
print(pos)

dire = 0

mov = [(0, -1), (1, 0), (0, 1), (-1, 0)]

visited = [pos]

while True:
    #grd = [list([list(c) for c in r]) for r in inp]
    (nx,ny) = (pos[0] + mov[dire][0], pos[1] + mov[dire][1])
    try:
        if inp[ny][nx] == '#':
            dire = (dire + 1) % 4
            continue
    except: pass
    #else:
        #grd[ny][nx] = '^'
    print(dire, nx,ny)
    pos = (nx, ny)
    if ny >= len(inp) or nx >= len(inp[0]) or ny < 0 or nx < 0:
        break
    visited += [pos]
    #print(grd)

print(len(set(visited)))
