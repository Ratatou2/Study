# 피타고라스 정리 -> 피타고라스 삼조

for c in range(200, 700):
    for b in range(200, 500):
        a = 1000 - b - c
        if not a < b < c:
            break
        else:
            if (a**2) + (b**2) == c ** 2:
                if a + b + c == 1000:
                    #print(a, b, c)
                    print(a*b*c)


# 아래와 같이 효율적으로 짤 수 있음
# a + b + c = 1000d이니까 바꿔 말하면 c = 1000 - b - a 란 뜻이기도 하다는 것을 기억하면 됨
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)