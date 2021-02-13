s = str(input())

def expand(left: int, right:int):
    if len(s)<2 or s==s[::-1]:
            return s
    while left >=0 and right<len(s) and s[left]==s[right]:
        left -=1
        right +=1
    return s[left+1:right]
# if len(s)%2==0:
#     expand(len(s)/2-1, len(s)/2)
# else:
#     expand(len(s)/2-1, len(s)/2)
result = ''
for i in range(len(s)-1):
    result = max(result, expand(i, i+1), expand(i, i), key=len)
print(result)