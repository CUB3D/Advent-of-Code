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
spos = pos
print(pos)

dire = 0

mov = [(0, -1), (1, 0), (0, 1), (-1, 0)]

visited = [pos]

ans = 0
for ty in range(len(inp)):
    for tx in range(len(inp[0])):
        if (tx, ty) == spos: continue
        visited = [pos]
        pos = spos
        dire = 0 
        while True:
            (nx,ny) = (pos[0] + mov[dire][0], pos[1] + mov[dire][1])
            try:
                if inp[ny][nx] == '#' or ny == ty and nx == tx:
                    dire = (dire + 1) % 4
                    continue
            except: pass
            pos = (nx, ny)
            if ny >= len(inp) or nx >= len(inp[0]) or ny < 0 or nx < 0:
                break
            if (dire, pos) in visited:
                print("lop", tx, ty)
                ans += 1
                break
            visited += [(dire, pos)]
print(ans)

