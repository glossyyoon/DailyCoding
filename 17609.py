import sys

T = int(sys.stdin.readline())


def palindrome(s, flag):
    hIdx = len(s) // 2
    hArr = s[:hIdx]
    if len(s) % 2 == 0:
        reverseArr = s[: hIdx - 1 : -1]
    else:
        reverseArr = s[:hIdx:-1]

    if hArr == reverseArr:
        if flag == 0:
            print(0)
            return True
        else:
            return True


def solution(s):
    flag = 0
    hIdx = len(s) // 2
    hArr = s[:hIdx]
    if palindrome(s, flag):
        return
    else:
        idx = 0
        flag = 1
        while idx < hIdx:
            n = -(idx + 1)
            if s[idx] != s[n]:
                sSubLeft = s[:idx] + s[idx + 1 :]
                sSubRight = s[: len(s) + n] + s[len(s) + n + 1 :]
                if palindrome(sSubLeft, flag) or palindrome(sSubRight, flag):
                    print(1)
                    return
                else:
                    print(2)
                    return
            else:
                idx += 1


while T > 0:
    s = sys.stdin.readline().rstrip()
    solution(s)
    T -= 1
