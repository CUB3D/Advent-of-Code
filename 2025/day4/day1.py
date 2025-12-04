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

def d(grd2):
    for yy in range(h):
            print("".join(grd2[yy]))
   
grd2 = list([list(x) for x in grid])


total = 0
for yyy in range(h):
    for xxx in range(w):
        if g(xxx, yyy) == '@':
            cnt = -1
            for oy in range(3):
                for ox in range(3):
                    if g(xxx+ox-1, yyy+oy-1) == '@':
                        cnt += 1
            if cnt < 4:
                total += 1
                grd2[yyy][xxx] = 'x'

d(grd2)
print(total)
            

