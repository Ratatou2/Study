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

'''
# 답안 예시
def consecutive_sum(start, end):
    # base case        
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
'''