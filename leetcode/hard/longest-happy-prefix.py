def longest_happy_prefix(string: str) -> str:
    answer = ""

    i = 1
    n = len(string)

    while i != n:
        prefix = string[:i:]
        suffix = string[n - i::]

        if prefix == suffix:
            answer = prefix

        i += 1

    return answer


print(longest_happy_prefix("level"))
print(longest_happy_prefix("ababab"))
