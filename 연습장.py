import re
def solution(new_id):
    answer1 = ''
    answer1 += new_id.lower()
    answer2 = re.sub('[^a-z | ^0-9|^.|^-|^_]','', answer1)
    answer = re.sub('[.{2,}]','', answer2)
    return answer
print(solution("...!@BaT#*..y.abcdefghijk-l_m99"))