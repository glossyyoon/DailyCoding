s1 = [1, 2, 3, 4, 5]
s2 = [2, 1, 2, 3, 2, 4]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answers = [1, 2, 3, 4, 5]
answer = [0, 0, 0]
for i in range(len(answers)):
    if i % (len(s1) - 1) == 0:
        s1 += s1
    if i % (len(s2) - 1) == 0:
        s2 += s2
    if i % (len(s3) - 1) == 0:
        s3 += s3

    if answers[i] == s1[i]:
        answer[0] += 1
    if answers[i] == s2[i]:
        answer[1] += 1
    if answers[i] == s3[i]:
        answer[2] += 1

maxx = max(answer)
count = 0
ans = []
for i in range(3):
    if answer[i] == maxx:
        count += 1
        ans.append(i + 1)
if count > 1:
    print(sorted(ans))
else:
    print(ans)
