def min_coin_count(value, coin_list):
    coin = list(reversed(sorted(coin_list)))
    count_coin = 0

    for i in range(len(coin)):
        count = value // coin[i]
        value -= count * coin[i]
        count_coin += count

    return count_coin


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))


# 다시 짜보기
total = 23520
coun = 0
for coin in sorted(default_coin_list, reverse=True):
    coun += total // coin
    total %= coin
print(total, coun)

'''
<< +a>>
- 리스트를 revered랑 정렬 적용해서 for문에 적용할 수 있음
for coin in sorted(coin_list, reversed=True):

위 코드를 효율적으로 짜면 아래와 같이 짤 수 있다

def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value // coin)

        # 잔액을 계산한다
        value %= coin

    return count

'''