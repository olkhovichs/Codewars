def count_nines(n):
    cnt = 0
    for i in range(n + 1):
        for x in str(i):
            cnt += x.count('9')
    return cnt