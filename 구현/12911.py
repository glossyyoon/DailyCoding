def solution(n):
    answer = 0
    num = n
    oneNum = bin(num).count("1")
    while True:
        num += 1
        if bin(num).count("1") == oneNum:
            return num
