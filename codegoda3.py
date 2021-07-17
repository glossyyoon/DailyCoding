from itertools import combinations


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N, M = map(int, input().split())
    agoji = []
    result = []
    count = 0
    for i in range(M):
        agoji.append(list(map(int, input().split())))
    agojis = []
    for i in range(len(agoji)):
        a, b = agoji[i]
        r = []
        for j in range(a, b + 1):
            r.append(j)
        agojis.append(r)
    result = 0
    i = 0
    j = 0
    while result != M:
        if i < M:
            result += agojis[i][j]
            i += 1
        elif j < M:
            result += agojis[i][j]
            j += 1
        count += 1
    print(count)
    return 0


if __name__ == "__main__":
    main()
