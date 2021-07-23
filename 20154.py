alpha = list(str(32123333113133122212112221))
s = list(input())
num_s = ""
c = 0

for i in range(len(s)):
    num_a = alpha[ord(s[i]) - ord("A")]
    c += int(num_a)
if c > 10:
    c %= 10
if c % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
# i = 0
# while len(num_s) != 1:
#     num_s[i] = str(int(num_s[i]) + int(num_s[i + 1]))
#     num_s[i + 1] = ""
# print(num_s)
