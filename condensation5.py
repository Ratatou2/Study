# 원본 내 코드
def is_palindrome(word):
    rebuild = list(word)
    rev = list(rebuild)
    rev.reverse()
    for i in range(len(rebuild)):
        if rebuild[i] != rev[i]:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))


# 이건 약간 꼼수를 쓴거라 시간이 좀 더 오래 걸림
# 아래 코드가 더 간결하고 깔끔한 버전
# 심지어
# rev = list(rebuild)
# rev.reverse()
# 위 부분을 rebuild = word[::-1] 하면 한큐에 해결됨...


def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1  # 맨 처음이랑 끝자락 -1이 더 있는건 리스트가 0부터 시작하니까
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))



# 공부 응용 최종
def is_palindrome(word):
    word_list = list(word)
    rev_list = list(word[::-1])

    if word_list != rev_list:
        return False

    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))