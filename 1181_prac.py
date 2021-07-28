n = int(input())
r = []
for i in range(n):
    s = input()
    count = len(s)
    r.append((len(s), s))
r = list(set(r))
r.sort(key=lambda word: (word[0], word[1]))
print(r)
for i in range(len(r)):
    print(r[i][1])
