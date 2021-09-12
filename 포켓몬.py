def solution(nums):
    answer = 0
    n = list(set(nums))
    if len(n) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(n)
