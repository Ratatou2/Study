# 피보나치  수열

count = 1
fibo_a = 1
fibo_b = 1
print(fibo_a)
print(fibo_b)
while count <= 48:
    fibo_a += fibo_b
    print(fibo_a)
    fibo_b += fibo_a
    print(fibo_b)
    count += 2


# 아래 코드는 임시저장소 temp를 만들어 previous를 저장해두고 curr를 prev로 옮기고 current는 prev의 원래 값(temp)과 current를 더한 값으로 이동한다
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1