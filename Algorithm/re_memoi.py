def max_profit_memo(price_list, count, cache):
    # 일단 0, 1 은 들어오면 그냥 바로 price_list에서 가져옴
    # 얘들은 조합을 계산할게 없으니까
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이건 후반부에 cache에 값이 좀 쌓이면 유용한 코드
    # cache에 값이 이미 있다면 바로 리턴한다
    if count in cache:
        return cache[count]

    # 조합식에서 가질 수 있는 maximum의 초기값을 설정
    # count가 len(price_list)보다 작으면 = count의 값이 price_list에 있다면
    # 해당값은 price_list에 있는 값을 먼저 가져옴, 인는 나중에 max를 적용할 떄 기준값이 되어줌
    if count < len(price_list):
        maximum = price_list[count]
    else:
        maximum = 0

    # for문을 돌리는데 (1,4ㅋ)와 (4,1)의 조합은 결국 같으니까 중복을 피하기 위해 count//2+1까지만 반복문 실행
    # 그러고 나면 아까 저앻준 maximum에 재귀 함수 결과값을 비교함
    # 재귀를 두번 도는데 i와 count-i로 돌린 것을 더하면 다음과 같은 조합들 전부 계싼해준다
    # ex) count가 7이면, (1,6), (2,5), (3,4) 와 같이 i가 커질수록 count-i는 작아지니 전부 계산 가능하다
    for i in range(1, count // 2 + 1):
        maximum = max(maximum, max_profit_memo(price_list, i, cache) +
                      max_profit_memo(price_list, count - i, cache))

    cache[count] = maximum  # count 일떄 구한 조합의 최대값을 cache에 등록해둠
    return maximum


def max_profit(price_list, count):
    max_cache = {}

    return max_profit_memo(price_list, count, max_cache)


print(max_profit([0, 100, 400, 850, 900, 1000], 4))
print(max_profit([0, 100, 400, 800, 9000, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
