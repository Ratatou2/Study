# 브루트포스 방식 사용
def sublist_max(profits):
    best_profit = []

    for start in range(len(profits)):
        for end in range(len(profits)):

            if len(profits[start:end]) > 0:
                # 0부터 5까지라고 하면 실질적으로 0부터 4번째 인덱스까지의 값만 더한다
                # 파이썬 리스트의 특징
                profit = sum(profits[start:end+1])
                best_profit.append(profit)

    return max(best_profit)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))