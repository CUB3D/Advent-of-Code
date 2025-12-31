import functools

inpu = open("input").readlines()
grid = [[x for x in y.strip()] for y in inpu]

h = len(grid)
w = len(grid[0])

def g(xxx, yyy):
    if xxx < 0 or yyy < 0: 
        return ''
    if yyy >= h or xxx >= w:
        return ''
    return grid[yyy][xxx]

def sg(xxx, yyy, v):
    if xxx < 0 or yyy < 0: 
        return ''
    if yyy >= h or xxx >= w:
        return ''
    grid[yyy][xxx] = v

def d(grd2):
    for yy in range(h):
            print("".join(grd2[yy]))

sx = grid[0].index('S')   

@functools.cache
def calc(xxx, yyy):
   if g(xxx, yyy) == '^':
        return calc(xxx - 1, yyy) + calc(xxx + 1, yyy)
   elif g(xxx, yyy) == '.' or g(xxx, yyy) == 'S':
        return calc(xxx, yyy+1)
   else:
        return 1

total = calc(sx, 0)
print(total)
