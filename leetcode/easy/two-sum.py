# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


def two_sum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) != i:
            return [i, nums.index(target - nums[i])]
