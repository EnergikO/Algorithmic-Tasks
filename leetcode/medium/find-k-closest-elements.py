
def get_index_of_closest_number_by_value_to_x(numbers: list[int], x: int) -> int:
    min_delta = abs(numbers[0] - x)
    index = 0

    for i in range(len(numbers)):
        if abs(numbers[i] - x) < min_delta:
            min_delta = abs(numbers[i] - x)
            index = i

    return index


def find_k_closest_elements_to_x(numbers: list[int], k: int, x: int) -> list[int]:
    """return the k closest integers to x in the array."""
    closest_numbers = []
    i = get_index_of_closest_number_by_value_to_x(numbers, x)
    closest_numbers.append(numbers[i])
    left = i - 1
    right = i + 1

    del i

    while len(closest_numbers) < k:

        try:
            if abs(numbers[left] - x) <= abs(numbers[right] - x):
                closest_numbers.append(numbers[left])
                left -= 1

            else:
                closest_numbers.append(numbers[right])
                right += 1

        except IndexError:
            closest_numbers.append(numbers[left])
            left -= 1

    return sorted(closest_numbers)


def test_case(numbers: list[int], k: int, x: int, answer) -> None:
    print(find_k_closest_elements_to_x(numbers, k, x))
    assert find_k_closest_elements_to_x(numbers, k, x) == answer

    print('Good.')


test_case([1,2,3,4,5], 4, 3, [1,2,3,4])
test_case([1,2,3,4,5], 4, -1, [1,2,3,4])
test_case([3,5,8,10], 2, 15, [8, 10])
