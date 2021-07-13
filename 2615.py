import sys

omok = list(sys.stdin.readline().split() for _ in range(19))
for i in range(19):
    for j in range(19):
        if omok[i][j] != "0":
            count = 1
            a = omok[i][j]
            si, sj = i, j
            while omok[i][j] == a and i < 19 and j < 19:
                if count == 5:
                    print(a)
                    print(si + 1, sj + 1)
                    exit(0)

                i += 1
                j += 1
                count += 1

            while omok[i][j] == a and i < 19 and j < 19:
                if count == 5:
                    print(a)
                    print(si + 1, sj + 1)
                    exit(0)
                i += 0
                j += 1
                count += 1

            while omok[i][j] == a and i < 19 and j < 19:
                if count == 5:
                    print(a)
                    print(si + 1, sj + 1)
                    exit(0)
                i += 1
                j += 0
                count += 1

            while omok[i][j] == a and i < 19 and j < 19:
                if count == 5:
                    print(a)
                    print(si + 1, sj + 1)
                    exit(0)
                i += 1
                j -= 1
                count += 1
print(0)
