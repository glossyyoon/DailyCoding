l, c = map(int, input().split())
a = input().split()
a.sort()


def go(n, alpha, password, i):
    #n = 만들어야하는 암호의 길이, alpha = 사용할 수 있는 알파벳
    #password = 만든 암호, i = 사용해야할지 말지를 결정할 인덱스
    if n == len(password):
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i + 1)
    go(n, alpha, password, i + 1)


def check(s):
    ja = 0
    mo = 0
    for i in s:
        if i in 'aeiou':
            mo += 1
        else:
            ja += 1
    if mo > 0 and ja >= 2:
        return True
    return False


go(l, a, "", 0)