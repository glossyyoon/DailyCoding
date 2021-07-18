import sys

N, M = map(int, sys.stdin.readline().split())
# 0과 1로 표시해야 비트연산자를 이용할 수 있음.
trains = [0] * N

for i in range(M):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 1:
        i, x = a[1] - 1, a[2] - 1
        trains[i] = trains[i] | 1 << x
    elif a[0] == 2:
        i, x = a[1] - 1, a[2] - 1
        trains[i] = trains[i] & ~(1 << x)
    elif a[0] == 3:
        i = a[1] - 1
        trains[i] = trains[i] << 1
        trains[i] = trains[i] & ~(1 << 20)

    elif a[0] == 4:
        i = a[1] - 1
        trains[i] = trains[i] >> 1
# print(trains)
print(len(set(trains)))
