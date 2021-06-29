def fib_optimized(n):
    cur = 1
    prev = 0

    if n < 3:
        return cur

    else:
        for i in range(2, n+1):
            cur, prev = cur + prev, cur
            print(i , cur, prev)
    return cur


print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))


'''
<<예시 답안>>

def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다. 
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다. 
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
'''