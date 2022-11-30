def generate_hashtag(s):
    if not s:
        return False
    res = []
    for i in s.split(' '):
        if i:
            res.append(i.title())
    if len(''.join(res)) > 140:
        return False
    return '#' + ''.join(res)