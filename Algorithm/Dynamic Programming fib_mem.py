def fib_memo(n, cache):
    if n < 3:
        return 1

    if n in cache:
        return cache[n]

    # 재귀를 씀으로 인해 fib_memo를 통해서 함수 fib의 fib_cache에 이전 값들을 전부 기록할 수 있는 기회를 줌
    cache[n] = fib_memo(n-2, cache) + fib_memo(n-1, cache)

    return cache[n]


def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))


# 내 코드는 피보나치 수열 자체를 구현해 버린셈
# memo안에 넣어두고 꺼내쓰는 방식으로 바꾸기