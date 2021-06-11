def max_product(left_cards, right_cards):
    remember = []
    for i in left_cards:
        for j in right_cards:
            remember.append(i * j)

    # remember.sort() # 사실상 정렬이 필요없음 max하면 리스트에서 최고값을 출력하니까
    return max(remember)


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))


# 모범답안
# 얘는 매번 갱신해줌
def max_product(left_cards, right_cards):
    # 현재까지 최댓값을 담기 위한 변수
    # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max_product = left_cards[0] * right_cards[0]

    # 가능한 모든 조합을 보기 위한 중첩 반복문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
            max_product = max(max_product, left * right)

    # 찾은 최댓값을 리턴한다
    return max_product