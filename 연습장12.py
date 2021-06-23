import collections
a = ["leo", "kiki", "eden"]
b = ["eden", "kiki"]
ans = collections.Counter(a) - collections.Counter(b)
print(list(ans.keys())[0])
