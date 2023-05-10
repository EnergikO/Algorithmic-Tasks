def find_middle_index(numbers: list[int]) -> int:
    def is_it_middle_index(index: int) -> bool:
        nonlocal numbers

        left_sum = sum(numbers[:index:])
        right_sum = sum(numbers[index + 1::])

        return left_sum == right_sum

    middle_index = -1

    for i in range(len(numbers)):
        if is_it_middle_index(i):
            middle_index = i
            break

    return middle_index


print(find_middle_index([2, 3, -1, 8, 4]))
print(find_middle_index([1, -1, 4]))
print(find_middle_index([2, 5]))
