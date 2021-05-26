i = 100

while True:
    if i % 23 == 0:
        print(i)
        break
    i += 1

# 위 코드를 아래처럼 간결하게 할 수 있음

while i % 23 != 0:  # i가 23으로 나눴을 때 나머지가 0이 아니면 계속 진행한단 소리
    i += 1