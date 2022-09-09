def is_pangram(s):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in alph:
        if i not in s:
            return False
    return True
    