def max_profit(price_list, count):
    record = []

    if count < 2:
        record.append(price_list[count])
        return price_list[count]

    if count < len(price_list):
        maximum = price_list[count]
    else:
        maximum = 0

    for i in range(1, count//2 + 1):
        maximum = max(maximum, max_profit(price_list, i) + max_profit(price_list, count - i))
        record.append(maximum)
    print(record)
    return max(record)


# 테스트
print(max_profit([0, 200, 600, 9000, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
