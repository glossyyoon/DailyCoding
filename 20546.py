import sys

money = int(sys.stdin.readline())
stock = list(map(int, sys.stdin.readline().split()))


def bnp(money):
    count = 0
    for i in range(14):
        if stock[i] <= money:
            count = money // stock[i]
            money = money % stock[i]
    lastStock = stock[-1]
    return money + count * lastStock


def timing(money):
    count = 0
    boughtStock = 0
    for i in range(10):
        if stock[i] < stock[i + 1] < stock[i + 2] < stock[i + 3] and count > 0:
            money += count * stock[i + 3]
            count = 0
        elif stock[i] > stock[i + 1] > stock[i + 2] > stock[
                i + 3] and money >= stock[i + 3]:
            count += money // stock[i + 3]
            money %= stock[i + 3]
            boughtStock = stock[i + 3]
    lastStock = stock[-1]
    return money + count * lastStock


if bnp(money) > timing(money):
    print("BNP")
elif bnp(money) < timing(money):
    print("TIMING")
else:
    print("SAMESAME")