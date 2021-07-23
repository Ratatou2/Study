def power(x, y):
    result = 1
    if y > 2:
        power(x, y-1)

    else:
        result *= x
        print(result)
        return result


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))