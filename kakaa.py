def solution(new_id):
    import re
    answer1 = ''
    answer1 += new_id.lower()
    print(answer1)
    answer = re.sub('[^0-9]|[^a-b]|.|-|_','', answer1)
    return answer
print(solution("ABC"))