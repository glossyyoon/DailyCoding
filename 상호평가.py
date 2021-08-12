def solution(scores):
    answer = ""
    stuNum = len(scores)
    for i in range(stuNum):
        arr = [0] * stuNum
        for j in range(stuNum):
            arr[j] = scores[j][i]
        me = arr[i]
        maxx = max(arr)
        minn = min(arr)
        count = 0
        if me == maxx:
            for q in range(len(arr)):
                if arr[q] == maxx:
                    count += 1
        elif me == minn:
            for q in range(len(arr)):
                if arr[q] == minn:
                    count += 1
        if count == 1:
            avg = (sum(arr) - me) / (len(arr) - 1)
        else:
            avg = sum(arr) / len(arr)
        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer


print(
    solution(
        [
            [100, 90, 98, 88, 65],
            [50, 45, 99, 85, 77],
            [47, 88, 95, 80, 67],
            [61, 57, 100, 80, 65],
            [24, 90, 94, 75, 65],
        ]
    )
)
