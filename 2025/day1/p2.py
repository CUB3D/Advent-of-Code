inp = open("input").readlines()


cnt = 50
day1 = 0
for l in inp:
   if l[0] == 'L':
    x = -1
   else:
    x = 1
   i = int(l[1:])
   for _ in range(i):
      cnt = (cnt + x) % 100
      if cnt == 0:
        day1 += 1

print(day1)
