import sys


def make_table(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j


def KMP(parent, pattern):
    make_table(pattern)
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    else:
        return False


parent = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
table = [0] * len(pattern)
if KMP(parent, pattern):
    print("1")
else:
    print("0")
