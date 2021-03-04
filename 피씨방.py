import sys


def main():
    comp, guest, timer = map(int, sys.stdin.readline().split())
    info = []
    result = 0
    for i in range(comp + 1):
        info.append([])
    for i in range(guest):
        num, times = map(int, sys.stdin.readline().split())
        info[num].append(times)

    def counter(computer, time):
        dp = [x for x in computer]
        counts = 0
        for i in range(len(computer)):
            for j in range(len(computer)):
                if computer[i] > computer[j]:
                    dp[i] = max(dp[i], dp[j] + computer[i])
        for d in range(len(dp)):
            if dp[d] <= time and counts < dp[d]:
                counts = dp[d]
        return counts

    for i in range(comp):
        print("%d" % (i + 1), counter(info[i + 1], timer) * 1000)


if __name__ == "__main__":
    main()