def solution(new_id):
    answer = ""
    special = ["-", "_", "."]
    l = list(new_id)
    for i in range(len(new_id)):
        if new_id[i].isupper():
            s = new_id[i].lower()
            l[i] = s
        if (
            not new_id[i].isalpha()
            and not new_id[i].isalnum()
            and not new_id[i] in special
        ):
            l[i] = ""

    for i in l:
        answer += i
    a = list(answer)
    result = "" + a[0]
    cur = a[0]
    for i in range(1, len(a)):
        if a[i] == cur:
            continue
        elif a[i] != " " and a[i] != cur:
            cur = a[i]
            result += cur
    print(result)
    a = result
    answer = ""
    for i in a:
        answer += str(i)
    print(answer)
    # 4
    if len(answer) >= 1 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == ".":
        answer = answer[:-1]
    # 5단계
    if answer == "":
        answer = "a"
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer = answer + answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
