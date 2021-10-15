def jinsu(n, jin):
    num = ""
    while n >= 1:
        number = n % jin
        if number == 10:
            number = "A"
        if number == 11:
            number = "B"
        if number == 12:
            number = "C"
        if number == 13:
            number = "D"
        if number == 14:
            number = "E"
        if number == 15:
            number = "F"
        num = str(number) + num
        n = n // jin
    return num


def solution(n, t, m, p):
    answer = ""
    count = 0
    head = p - 1
    binary = "0"
    while len(answer) != t:
        binary += str(jinsu(count, n))
        if head > len(binary) - 1:
            count += 1
            binary += str(jinsu(count, n))
            answer += binary[head]
            head += m
            count += 1
            continue
        answer += binary[head]
        count += 1
        head += m
    return answer


solution(16, 16, 2, 2)
