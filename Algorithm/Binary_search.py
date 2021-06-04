# 개선사항 : 그 이전 코드는 for문의 범위 때문에 답을 찾았음에도 계속 도는 비효율 발생
# 이를 해결하고자 모범 답안의 코드를 공부하였음

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) -1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        print(start_index, end_index)

        if some_list[mid] == element:
            return mid

        elif some_list[mid] > element:
            end_index = mid -1

        elif some_list[mid] < element:
            start_index = mid + 1


# def binary_search(element, some_list):
#     start_index = 0
#     end_index = len(some_list) - 1
#     count = 0
#
#     while start_index <= end_index:
#         count += 1
#         print(count)
#         midpoint = (start_index + end_index) // 2
#         if some_list[midpoint] == element:
#             return midpoint
#         elif some_list[midpoint] > element:
#             end_index = midpoint - 1
#         else:
#             start_index = midpoint + 1
#     return None


print(binary_search(5, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53]))


# def binary_search(element, some_list):
#     mid = len(some_list) // 2
#
#     for i in range(len(some_list)-1):
#         if some_list[mid] == element:
#             return mid
# 
#         elif some_list[mid] > element:
#             mid = mid // 2
#
#         elif some_list[mid] < element:
#             mid = (mid + len(some_list)) // 2
#
# '''
# elif some_list[mid] < element:
#     return mid = mid + len(some_list)-1) // 2)
#
# 이렇게 풀면 마지막 print(binary_search(11, [2, 3, 5, 7, 11])) 가 작동하지 않는다
# 그 이유는 반올림이 안되어서 마지막 7과 11을 비교할때 둘의 인덱스 값인 3 + 4 한후 // 2로 몫을 구하게 되는데
# 반올림이 적용되지 않으므로 계속 3이 나와서 결국 답을 찾을 수 없다
#
# 이를 해결하기 위해선 round함수를 쓰거나 len(some_list)에서 -1을 빼지 않고, 진행하는 경우가 있다
# round는 파이썬 전용이기 때문에 배제하고 생각한다면, len(some_list)에서 -1을 빼지 않으므로 인해 + 1 해주는 효과를 얻을 수 있다.
# '''
#
# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))