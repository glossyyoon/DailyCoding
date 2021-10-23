def productExceptSelf(nums):
    answers1 = [1] * len(nums)
    answers2 = [1] * len(nums)
    for i in range(1, len(nums)):
        answers1[i] = nums[i - 1] * answers1[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        answers2[i] = nums[i + 1] * answers2[i + 1]
    return [answers1[i] * answers2[i] for i in range(len(nums))]


print(productExceptSelf([1, 2, 3, 4]))
