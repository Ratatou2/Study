# 개선 사항 mid_index가 답이 아니라는 것은 전체 길이에서 mid_index도 빼도 된다는 소리임
# 즉 start_inedx나 end_index에 mid를 줄떄 mid-1을 하면 된단 소리
# 또한 mid-1을 했으니 전체길이도 -1 이므로 round처리 해줄 필요없이 // 으로 몫을 바로 구하면 된다
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    mid_index = round((start_index + end_index) / 2)

    if some_list[mid_index] == element:
        return mid_index

    elif some_list[mid_index] > element:
        print(start_index, end_index)
        if len(some_list[:mid_index]) == 0:
            return None
        return binary_search(element, some_list, 0, mid_index)

    elif some_list[mid_index] < element:
        print(start_index, end_index)
        if len(some_list[mid_index:]) == 0:
            return None
        return binary_search(element, some_list, mid_index, None)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))




# 모범답안
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None

    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2

    # 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))