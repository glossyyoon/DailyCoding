from itertools import combinations

nums = [1, 2, 3, 4]


def sosu(num):
    n = 2
    while True:
        if n == num:
            return True
        if num % n == 0:
            return False
        n += 1


result = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            a, b, c = nums[i], nums[j], nums[k]
            if sosu(a + b + c):
                result += 1
print(result)
