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
        for _ in list2[j:]:
            merg_list.append(list2[j])
            j += 1
        # 위의 세줄 merg_list += list2[j:] 로 수정 가능
        
    else:
        for _ in list1[i:]:
            merg_list.append(list1[i])
            i += 1

    return merg_list


print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

'''
<<위의 for문>>
for _ in list2[j:]:
    merg_list.append(list2[j])
    j += 1
을 깔끔하게

merg.list += list2[j:]
로 바꿀수 있음    
    
'''