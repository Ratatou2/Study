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
    print(numbers)
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []

    while True:
        if len(new_guess) == 3: break
        print(f"{len(new_guess)+1}번째 숫자를 입력하세요: ", end='')
        user_num = int(input())

        if user_num not in range(0, 10):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요')
        elif user_num in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        else: new_guess.append(user_num)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in guess:
        if i in solution and guess.index(i) == solution.index(i):
            strike_count += 1
        elif i in solution:
            ball_count += 1

    return strike_count, ball_count


# # 테스트
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)
#
# s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
# print(s_2, b_2)
#
# s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
# print(s_3, b_3)
#
# s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
# print(s_4, b_4)



# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user = take_guess()
    tries += 1
    if get_score(user, ANSWER)[0] == 3:
        break
    print(f'{get_score(user, ANSWER)[0]}S {get_score(user, ANSWER)[1]}B\n')


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))



# 모범답안
from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def take_guess():
    new_guess = []
    while len(new_guess) < 3:
        num = int(input("{}번째 수를 입력하세요: ".format(len(new_guess) + 1)))

        if num < 0 or num > 9:
            print("0에서 9까지의 수를 입력해 주세요!")
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)

    return new_guess


def get_score(guess, answer_list):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == answer_list[i]:
            strike_count += 1
        elif guess[i] in answer_list:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))





