import sys

n = int(sys.stdin.readline())
func = sys.stdin.readline()
nums = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
for i in func:
    if i.isalpha():
        stack.append(nums[ord(i) - ord('A')])
    else:
        if i == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif i == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        elif i == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif i == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

for i in stack:
    print("%.2f" % i)
