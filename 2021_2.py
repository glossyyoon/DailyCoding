import math


def isPrime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    n = int(n)
    changedNum = ""
    while n > 1:
        changedNum += str(int(n) % k)
        n = int(n)
        n //= k
    changedNum = changedNum[::-1]
    if n == 1:
        changedNum = "1" + changedNum
    numList = list(changedNum.split("0"))
    for i in numList:
        if i != "" and int(i) != 1 and isPrime(i):
            answer += 1
    return answer


print(solution("437674", 3))
