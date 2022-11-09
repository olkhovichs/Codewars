from collections import Counter

def score(dice):
    dices = Counter(dice)
    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)
    total = 0
    for i, j in dices.items():
        if j >= 3:
            total += points[i] * (j // 3)
        if i == 1:
            total += 100 * (j % 3)
        elif i == 5:
            total += 50 * (j % 3)
    return total