def sum_in_list0(search_sum, sorted_list):

    for i in reversed(sorted_list):
        guess_num = search_sum - i

        if guess_num in sorted_list:
            return True

    return False


def sum_in_list(search_sum, sorted_list):

    while True:
        if len(sorted_list) == 0:
            return False

        check_last = sorted_list.pop()
        guess_num = search_sum - check_last

        if guess_num in sorted_list:
            return True


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))


# 해답 코드
# 젤 마지막 값과 맨 처음값을 더해서 찾는 값보다 크면 끝값을 줄이고, 작으면 맨 앞값을 늘인다.
def sum_in_list1(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum: # 합이 찾으려는 숫자일 때
            return True

        if candidate_sum < search_sum:  # 합이 찾으려는 숫자보다 작을 때
            low += 1

        else: # 합이 찾으려는 숫자보다 클 때
            high -= 1

    # 찾는 조합이 없기 때문에 False 리턴
    return False


# 테스트
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))