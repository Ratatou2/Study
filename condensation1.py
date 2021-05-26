
year = 1988
today_year = 2016

money = 50000000
miran = 1100000000

while year < 2016:
    money = money * 1.12
    year += 1

diff = int(money-miran)

if diff > 0:
    print(f"{diff}원 차이로 동일 아저씨 말씀이 맞습니다")
else : print(f"{diff}원 차이로 미란 아주머니 말씀이 맞습니다")


# 위 코드를 아래처럼 깔끔하게 개선할 수 있다


# 상수는 대문자로 쓰기
year = 1988
TODAY_YEAR = 2016

money = 50000000
MIRAN = 1100000000

while year < TODAY_YEAR:
    money = money * 1.12
    year += 1

diff = int(money-MIRAN)

if diff > 0:
    print(f"{diff}원 차이로 동일 아저씨 말씀이 맞습니다")
else : print(f"{diff}원 차이로 미란 아주머니 말씀이 맞습니다")
