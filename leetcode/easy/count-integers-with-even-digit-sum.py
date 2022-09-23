
# Given a positive integer num, return the number 
# of positive integers less than or equal to num 
# whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.

# Example:

# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal 
# to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.


def get_sum_of_digits(number: int) -> int:
        _sum = 0
        while number > 0:
            digit = number % 10
            _sum += digit
            number //= 10

        return _sum


def countEven(number: int) -> int:
    counter = 0
    for i in range(1, number + 1):
        if get_sum_of_digits(i) % 2 == 0:
            counter += 1

    return counter


print(countEven(30))
