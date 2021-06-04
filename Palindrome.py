def is_palindrome(word):
    check_pal = list(word)

    for i in range(len(check_pal)//2):
        if check_pal[i] != check_pal[-(i+1)]:
            return False

    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))