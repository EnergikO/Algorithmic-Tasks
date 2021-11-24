# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longestCommonPrefix(words: list) -> str:
	""":parameter words list[str]"""
	if not words:
		return ''

	letters = iter(list(max(words)))
	answer = str()

	while len(answer) != len(max(words)):
		actual_letter = letters.__next__()

		for word in words:
			if not word.startswith(answer + actual_letter):
				return answer

		answer += actual_letter

	return answer
