def solution(arr1, arr2):
    answer = []
    arr2 = list(map(list, zip(*arr2)))
    for i in range(len(arr1)):
        mul = []
        for k in range(len(arr2)):
            m = 0
            for j in range(len(arr1[i])):
                m += arr1[i][j] * arr2[k][j]
            mul.append(m)
        answer.append(mul)
    return answer


print(solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]))
