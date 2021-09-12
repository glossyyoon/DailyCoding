import math


def count(num):
    count = 0
    nums = []

    for i in range(1, int(math.sqrt(num)) + 1):
        print(i)
        if num % i == 0:
            count += 2
            nums.append(i)
    if num % (math.sqrt(num)) == 0:
        count -= 1
    return count


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if count(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
