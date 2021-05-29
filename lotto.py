# generate_numbers
# 이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다.

import random

def generate_numbers(n):
    random_list = []

    for i in range(n):
        random_int = random.randint(1, 45)
        random_list.append(random_int)

    return random_list

print('generate', generate_numbers(6))

# draw_winning_numbers
# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.

def draw_winning_numbers():
    winning_num = []
    for i in range(6):
        random_int = random.randint(1, 45)
        winning_num.append(random_int)

    winning_num.sort()
    random_int = random.randint(1, 45)
    winning_num.append((random_int))

    return winning_num
print('draw', draw_winning_numbers())



# count_matching_numbers
# 파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.

def count_matching_numbers(list1, list2):
    count = 0

    for i in list1:
        for j in list2:
            if i == j:
                count += 1

    return count

print(count_matching_numbers([1,2,3,4,5,7,8], [1,3,4,5,8,9]))


# check
# 참가자의 당첨 금액을 리턴합니다. 파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요. numbers는 당연히 번호 여섯 개를 담고 있고, winning_numbers는 보너스까지 해서 번호 7개를 담고 있겠죠?

# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)


def check(list1, list2):
    count = 0
    special = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1

    for i in list1:
        if i == list2[-1] : special += 1

    if count == 3: return 5000
    elif count == 4: return 50000
    elif special == 1 and count == 6: return 50000000
    elif count == 5: return 1000000

    elif count == 6: return 1000000000

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))


# 아래는 모범 답안

from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0











