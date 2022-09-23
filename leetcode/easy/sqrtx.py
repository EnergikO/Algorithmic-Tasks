# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

def binary_search_sqrt(number):
	left = 1
	right = number

	while left <= right:
		middle = (right + left) // 2

		if middle * middle == number:
			return middle

		elif middle * middle < number:
			left = middle+1

		else:
			right = middle-1

	return right


def mySqrt(x: int) -> int:
	return binary_search_sqrt(x)
