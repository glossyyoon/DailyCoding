import collections
a = [1, 2, 3, 3, 4, 5, 5,5, 5, 5, 6 ,7 , 8, 9]
b = collections.Counter(a)
print(b)
print(type(b))