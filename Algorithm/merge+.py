def merge(list1, list2):
    merg_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merg_list.append(list2[j])
            j += 1
        else:
            merg_list.append(list1[i])
            i += 1

    if i == len(list1):
        merg_list += list2[j:]
    else:
        merg_list += list1[i:]

    return merg_list


# 합병 정렬
def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list

    half = int(len(my_list) / 2)
    half_left = my_list[:half]
    half_right = my_list[half:]

    half_left = merge_sort(half_left)
    half_right = merge_sort(half_right)

    return merge(half_left, half_right)


print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
#print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
#print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


'''
모범답안
def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


def merge_sort(my_list):
    # base case
    if len(my_list) < 2:
        return my_list

    # my_list를 반씩 나눈다(divide)
    left_half = my_list[:len(my_list)//2]    # 왼쪽 반
    right_half = my_list[len(my_list)//2:]   # 오른쪽 반

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left_half), merge_sort(right_half))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))'''