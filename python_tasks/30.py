def split_strings(str):
    res = [str[i:i+2] for i in range(0, len(str), 2)]
    if len(str) % 2 == 0:
        return res
    else:
        res[-1] = res[-1] + '_'
        return res
