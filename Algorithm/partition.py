# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    small_group = []
    big_group = []

    pibot = my_list[end]

    for i in range(len(my_list)):
        if my_list[i] > pibot:
            big_group.append(my_list[i])

        elif my_list[i] <= pibot:
            small_group.append(my_list[i])

    new = small_group + [pibot] + big_group
    return new, new.index(my_list[end])


list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
