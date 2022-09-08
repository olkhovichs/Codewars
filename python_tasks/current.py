def parts_sums(ls):
    res = []
    for i, item in enumerate(ls):
        res.append(sum(ls[i:]))
    res.append(0)
    return res