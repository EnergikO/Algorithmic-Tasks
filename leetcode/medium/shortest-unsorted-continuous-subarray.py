def find_unsorted_subarray(numbers: list[int]) -> int:
    numbers_dict = {i: 0 for i in range((-10) ** 5, 10 ** 5 + 1)}
    first = None
    last = None

    for number in numbers:
        numbers_dict[number] += 1

    i = 0
    pairs = numbers_dict.items()
    for pair in pairs:
        number = pair[0]
        count = pair[1]

        if count == 0:
            continue

        for j in range(count):
            if first is None:
                if numbers[i] != number:
                    first = i

            if numbers[i] != number:
                last = i
            i += 1

    try:
        return last - first + 1
    except TypeError:
        return 0


print(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))
print(find_unsorted_subarray([1, 2, 3, 4]))
print(find_unsorted_subarray([1]))
print(find_unsorted_subarray([2, 1]))
print(find_unsorted_subarray([1, 3, 2, 2, 2]))
