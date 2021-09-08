def solution(numbers, hand):
    result = ""
    left = [1, 4, 7, "*"]  # 0, 1, 2
    right = [3, 6, 9, "#"]
    middle = [2, 5, 8, 0]
    l, r = "*", "#"
    n = 0
    for num in numbers:
        if num in left:
            l = num
            result += "L"
        elif num in right:
            r = num
            result += "R"
        else:
            # 거리계산
            # 입력받은 문자가 middle일 때,
            if l in middle and r in middle:
                dist_l = abs(middle.index(num) - middle.index(l))
                dist_r = abs(middle.index(num) - middle.index(r))
            elif l in middle:
                dist_l = abs(middle.index(num) - middle.index(l))
                dist_r = abs(middle.index(num) - right.index(r)) + 1
            elif r in middle:
                dist_r = abs(middle.index(num) - middle.index(r))
                dist_l = abs(middle.index(num) - left.index(l)) + 1
            else:
                dist_l = abs(middle.index(num) - left.index(l))
                dist_r = abs(middle.index(num) - right.index(r))
            # 손가락 할당
            if dist_l == dist_r and hand == "left":
                l = num
                result += "L"
            elif dist_l == dist_r and hand == "right":
                r = num
                result += "R"
            elif dist_l < dist_r:
                l = num
                result += "L"
            elif dist_r < dist_l:
                r = num
                result += "R"
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
"LRLLLRLLRRL"
