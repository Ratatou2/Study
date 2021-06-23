# Divide and Conquer
def consecutive_sum(start, end):

    if start == end:
        return start

    half = int((start + end) / 2)

    front = consecutive_sum(start, half)
    back = consecutive_sum(half+1, end)

    return front + back


print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))