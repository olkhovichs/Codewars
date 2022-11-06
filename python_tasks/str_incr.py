def increment_string(strng):
    letters = strng.rstrip('1234567890')
    numb = strng[len(letters):]
    if strng.isalpha() or not strng:
        return strng + '1'
    else:
        return letters + str(int(numb) + 1).zfill(len(numb))