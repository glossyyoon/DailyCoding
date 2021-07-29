n = int(input())
r = []
for i in range(n):
    s = input()
    r.append((len(s), s))
r = list(set(r))
r.sort(key=lambda word: (word[0], word[1]))
for i in range(len(r)):
    print(r[i][1])
