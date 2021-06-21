nums = [0 for i in range(30)]
for j in range(28):
    num = int(input())
    nums[num - 1] = 1
for n in range(len(nums)):
    if not nums[n]:
        print(n + 1)
