from itertools import permutations


def solution(n, k):
    print(list(permutations(range(1, n + 1), k)))


solution(4, 2)
