def find_same_number(some_list):
    for i in some_list:
        count_num = some_list.count(i)
        if count_num > 1:
            return i


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))


# 밑의 모범 답안에서는 사전에 이미 있는 값이면 바로 리턴하면서 끝남
# 내 코드처럼 전체를 카운트 할 필요 없으므로 더 적은 시간이 소요됨
def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True


print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))


# 아래가 스스로 짜본 코드
# 사전에 있기만하면 바로 리턴한다
def find_same_number(some_list):
    count_dic = {}
    for i in some_list:
        print(count_dic)
        if i in count_dic:
            return i

        count_dic[i] = 0


print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))