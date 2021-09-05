def isPrimeNum(num):
    n = 2
    if num == 2 or num == 3:
        return True
    while n != num:
        if num % n == 0:
            return False
        else:
            n += 1
            num
    return True


def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                curr = nums[i] + nums[j] + nums[k]
                if isPrimeNum(curr):
                    answer += 1

    return answer
