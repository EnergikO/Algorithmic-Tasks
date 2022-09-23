# You are given a sorted array consisting of only integers where every element appears exactly
# twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.


def binary_search(array, target):
    left = 0
    right = len(array)

    while right - left > 1:
        middle = (right + left) // 2

        if array[middle] > target:
            right = middle
        else:
            left = middle

    return array[left] is target


def solution_O_logN(array):
    for i in range(len(array)):
        target = array[i]
        arr_copy = array.copy()
        arr_copy.pop(i)

        if not binary_search(arr_copy, target):
            return target


def solution_best_time(array):
    if len(nums) == 1:
        return nums[0]

    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] < nums[i+1]:
            return nums[i]
    
    if nums[0] != nums[1]:
        return nums[0]
    Public
    if nums[-1] != nums[-2]:
        return nums[-1]
