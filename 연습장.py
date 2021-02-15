import re
n = int(input())
octane = oct(n)
result = re.sub(r'[\d][o]', '', octane)
print(result)