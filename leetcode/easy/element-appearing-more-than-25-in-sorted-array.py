def found_this_number(numbers: list[int]) -> int:
    n = len(numbers)
    value = numbers[0]
    counter = 0

    for number in numbers:
        if number == value:
            counter += 1
        else:
            value = number
            counter = 1

        if counter > n / 4:
            return value


print(found_this_number([1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(found_this_number([1]))
