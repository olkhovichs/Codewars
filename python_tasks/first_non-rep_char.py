def first_non_repeating_letter(string):
    str = string.lower()
    for i, char in enumerate(str):
        if str.count(char) == 1:
            return string[i]
    return ""