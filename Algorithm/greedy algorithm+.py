def max_product(card_lists):
    result = 1
    for cards in card_lists:
        result *= max(cards)

    return result


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))


'''
def max_product(card_lists):
    result = 1
    for cards in card_lists:
        for card in sorted(cards, reverse=True):
            result *= card
            break

    return result
    
위의 두번째 for문은 안에 있는 리스트에서 최댓값을 찾는 용도인데 다음과 같이 짜면
깔끔하고도 섹시하게 요약할수 있다

for cards in card_lists:
    result *= max(cards)
     

<해답코드>
def max_product(card_lists):
    # 누적된 곱을 저장하는 변수
    product = 1

    # 반복문을 돌면서 카드 뭉치를 하나씩 본다
    for card_list in card_lists:
        # product에 각 뭉치의 최댓값을 곱해 준다
        product *= max(card_list)

    return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
'''