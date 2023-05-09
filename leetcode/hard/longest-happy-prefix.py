def longest_happy_prefix(string: str) -> str:
    answer = ""

    n = len(string)
    i = n - 1

    while i != 0:
        prefix = string[:i:]
        suffix = string[n - i::]

        if prefix == suffix:
            answer = prefix
            break

        i -= 1

    return answer


print(longest_happy_prefix("level"))
print(longest_happy_prefix("ababab"))
