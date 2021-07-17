def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    n = int(input())
    arr = [0 for _ in range(96339173)]
    days = []
    for i in range(n):
        inn, out = input().split()
        y1, m1, d1 = inn.split("-")
        inn_date = int(y1 + m1 + d1)
        y2, m2, d2 = out.split("-")
        out_date = int(y2 + m2 + d2)
        days.append([inn_date, out_date])
    days = sorted(days)
    for i in range(n):
        inn_date = days[i][0]
        out_date = days[i][1]
        for k in range(out_date - inn_date):
            arr[inn_date - days[0][0] + k] += 1
    max_day = str(days[0][0] + arr.index(max(arr)))
    result = max_day[:4] + "-" + max_day[4:6] + "-" + max_day[6:]
    print(result)
    return 0


if __name__ == "__main__":
    main()
