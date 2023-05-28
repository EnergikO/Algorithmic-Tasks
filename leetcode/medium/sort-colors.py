def sort_colors(nums: list[int]) -> None:
    colors = {
        0: 0,
        1: 0,
        2: 0,
    }

    for number in nums:
        colors[number] += 1

    for i in range(len(nums)):
        if colors[0]:
            nums[i] = 0

        elif colors[1]:
            nums[i] = 1

        else:
            nums[i] = 2
