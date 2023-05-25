def merge_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    merged_array = []
    i = 0
    j = 0

    while len(merged_array) != m + n:
        if i == m:
            merged_array += nums2[j:m:]
            break

        if j == n:
            merged_array += nums1[i::]
            break

        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1
        else:
            merged_array.append(nums2[j])
            j += 1

    # The final sorted array should not be returned by the function,
    # but instead be stored inside the array nums1
    nums1 = merged_array.copy()

    return None


assert merge_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
