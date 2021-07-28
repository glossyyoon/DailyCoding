origin = input()
ans = input()
t = ""
for i in origin:
    if i.isalpha():
        t += i
if ans in t:
    print(1)
else:
    print(0)
