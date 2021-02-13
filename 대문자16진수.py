import re
n = int(input())
result = hex(n)
results = re.sub(r'[\d][x]', '', result)
print(results.upper())