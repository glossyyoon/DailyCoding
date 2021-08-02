import sys

T = int(sys.stdin.readline())

alphabet = [0] * 26
word = ""


def duplicate(w, k, q, s, word):
    k -= 1
    if k == 0:
        print("k==0", s)
        return s
    else:
        while w[q] != word and q < len(w):
            s += w[q]
            q += 1
        if str(w[q]) == str(word):
            s += w[q]
            k -= 1
        else:
            return

        if k > 0:
            duplicate(w, k, q, s, word)
        else:
            return s


def three(w, k):
    result = []
    for i in range(len(w)):
        n = ord(w[i]) - ord("a")
        alphabet[n] += 1
    for i in range(26):
        if alphabet[i] >= k:
            word = chr(i + ord("a"))
            s = ""
            for q in range(len(w)):
                if w[q] == word and q < len(w) - 1:
                    s += w[q]
                    q += 1
                    result.append(duplicate(w, k, q, s, word))
                    break
            # result.append(s)
    print(result)
    if result:
        result.sort(key=lambda x: len(x))
        return len(result[0])
    return -1


# def four(w, k):


for i in range(T):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    print(three(w, k))
