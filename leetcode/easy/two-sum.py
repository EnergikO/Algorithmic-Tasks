def two_sum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) != i:
            return [i, nums.index(target - nums[i])]

print(two_sum([-1,-2,-3,-4,-5], -8))
