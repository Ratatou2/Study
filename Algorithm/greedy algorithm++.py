def min_fee(pages_to_print):
    total_fee = 0
    pages_to_print = sorted(pages_to_print)

    for i in range(len(pages_to_print)):
        total_fee += pages_to_print[i] * len(pages_to_print[i:])
        # print(pages_to_print[i], pages_to_print[i:])

    return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

'''
<모범답안.
답안에서는 나처럼 슬라이스한 리스트의 길이를 구한게 아님
전체 리스트 길이에서 i를 빼줌 깔-끔

def min_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
'''