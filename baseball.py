from random import randint


def generate_numbers():
    numbers = []

    while True:
        random_num = randint(0, 9)

        if len(numbers) < 3:
            if random_num not in numbers:
                numbers.append(random_num)
        else: break

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 아래 코드는 while문에 애초에 조건을 줘서 깔끔하게 짠 코드
from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers