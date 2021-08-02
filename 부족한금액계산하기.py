def solution(price, money, count):
    result = 0
    for i in range(1, count + 1):
        result += i * price
    answer = result - money
    if answer <= 0:
        return 0
    return answer
