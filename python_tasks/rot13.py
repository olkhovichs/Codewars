def rot13(message):
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for i in message:
        index = alph.find(i)
        if index <= 12 or 25 < index <= 38:
            new_index = index + 13
        elif 12 < index <= 25 or index > 38:
            new_index = index - 13
        if i in alph:
            res += alph[new_index]
        else:
            res += i
    return res