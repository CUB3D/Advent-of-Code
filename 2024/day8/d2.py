inp = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........""".split("\n")

inp = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##""".replace('#', '.').split("\n")

inp = open("input").read().split("\n")[:-1]

w = len(inp)
h = len(inp[0])

nodes = []
for y in range(h):
    for x in range(w):
        if inp[y][x] == '.': continue

        r = []
        for ny in range(h):
            for nx in range(w):
                if inp[ny][nx] == inp[y][x]:

                    for o in range(2000):
                        an_x = nx + (nx-x)*o
                        an_y = ny + (ny-y)*o
                        
                        if 0 <= an_x < w and 0 <= an_y < h:
                            r += [(an_x, an_y)]
        nodes += set(r)
        print((x,y), r)
    


ans = len(set(nodes))
print(ans)
