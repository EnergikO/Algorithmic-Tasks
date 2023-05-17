def seconds_to_remove_occurrences(string: str) -> int:
    seconds = 0

    while string.count("01"):
        string = string.replace("01", "10")
        seconds += 1

    return seconds


print(seconds_to_remove_occurrences("0110101"))
print(seconds_to_remove_occurrences("11100"))
