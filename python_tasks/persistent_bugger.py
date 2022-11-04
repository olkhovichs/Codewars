import math

def persistence(n):
    count = 0
    while n > 9:
        n = math.prod(map(int, str(n)))
        count += 1
    return count