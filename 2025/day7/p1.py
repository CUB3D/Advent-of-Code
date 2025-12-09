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
   
total = 0
for yyy in range(h):
    for xxx in range(w):
        if g(xxx, yyy) == 'S' or g(xxx, yyy) == '|':
            if g(xxx, yyy+1) == '.':
                sg(xxx, yyy+1, '|')
            if g(xxx, yyy+1) == '^':
                sg(xxx+1, yyy+1, '|')
                sg(xxx-1, yyy+1, '|')
                total += 1


d(grid)
print(total)
            

