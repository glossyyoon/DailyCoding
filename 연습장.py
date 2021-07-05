left, right = input().split()
strings = list(input())

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'

xl, yl, xr, yr = None, None, None, None

for i in range(len(keyboard)):
    if left in keyboard[i]:
        xl = i
        yl = keyboard[i].index(left)

    if right in keyboard[i]:
        xr = i
        yr = keyboard[i].index(right)

time = 0
for string in strings:
    time += 1
    for j in range(3):
        if string in keyboard[j]:
            nx = j
            ny = keyboard[j].index(string)
            time += abs(xl - nx) + abs(yl - ny)
            xl = nx
            yl = ny
            break
        elif string in mo[j]:
            nx = j
            ny = mo[j].index(string)
            time += abs(xr - nx) + abs(yr - ny)
            xr = nx
            yr = ny
            break

print(time)