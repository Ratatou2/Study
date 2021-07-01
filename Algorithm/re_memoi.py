def max_profit_memo(price_list, count, cache):
    # 제일 작은 수에서 최대 조합법을 찾는다
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이 코드는 여기서 필요없음
    # if count in cache:
    #     print("BAM" + price_list.index(count))

    # price_list에 count에 해당하는 가격이 있다면 그 값을 profit에 넣어둠
    # 넣어둔 값의 없으면 그냥 0으로 줌
    # 넣어둔 값은 이따가 max로 비교할 떄 쓰임
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        maximum = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    print(maximum)
    return maximum


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


#print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
#print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
