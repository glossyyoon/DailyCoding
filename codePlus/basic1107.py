channel = int(input())
n = int(input())
a = list(map(int, input().split()))
button = [False] * 10
for i in a:
    button[i] = True  #고장난 버튼을 True로 바꿔줌.


def possible(c):
    if c == 0:
        if button[c] == False:
            return 1
        else:
            return 0
    l = 0
    while c > 0:
        if button[c % 10]:
            return 0
        c //= 10
        l += 1
    return l


ans = abs(n - 100)  #정답의 초기값
for i in range(1, 1000000 + 1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c - channel)
        if ans > l + press:
            ans = l + press
print(ans)