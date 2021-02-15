background = [
    [0 for cols in range(10)]
    for widths in range(10)
]
# 배경 input
for i in range(10):
    num = input().split()
    background[i] = list(map(int, num))

i = 1
j = 1
while background[i][j] != 2:
    