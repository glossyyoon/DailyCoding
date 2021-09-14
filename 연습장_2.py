def shiftingLetters(s, shifts) -> str:
    answer = [0 for _ in range(len(s))]
    n = 0
    for shift in range(len(shifts)):
        for i in range(n + 1):
            if answer[i] == 0:
                if ord(s[i]) + shifts[shift] > ord("z"):
                    answer[i] = ord(s[i]) + shifts[shift] - ord("z") + ord("a") - 1
                else:
                    answer[i] = ord(s[i]) + shifts[shift]
            else:
                if ord(s[i]) + shifts[shift] > ord("z"):
                    answer[i] += shifts[shift] - (ord("z")) + ord("a") - 1
                else:
                    answer[i] += shifts[shift]
        n += 1
        a = ""
    print(answer)
    for ans in answer:
        a += chr(ans)
    return a


print(shiftingLetters("abc", [3, 5, 9]))
print(shiftingLetters("bad", [10, 20, 30]))
