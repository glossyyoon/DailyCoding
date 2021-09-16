def jinsu(num, n):
    num_2 = ""
    while num >= 1:
        num_2 += str(num % 2)
        num //= 2
    if len(num_2) != n:
        num_2 = num_2 + "0" * (n - len(num_2))
    return num_2[::-1]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = ""
        num1 = list(jinsu(arr1[i], n))
        num2 = list(jinsu(arr2[i], n))
        for j in range(n):
            num += "#" if int(num1[j]) or int(num2[j]) else " "
        answer.append(num)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
