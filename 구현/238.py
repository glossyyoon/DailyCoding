def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    num = 1
    for i in range(len(nums)):
        answer.append(num)
        num = num * nums[i]
    num = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] = answer[i] * num
        num = num * nums[i]

    return answer
