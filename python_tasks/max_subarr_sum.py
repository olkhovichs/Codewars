def max_sequence(arr):
    if not arr or all(map(lambda x: x < 0, arr)):
        return 0
    curr_sum = arr[0]
    max_sum = curr_sum
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum