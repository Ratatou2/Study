# 1 1 2 3 5 8 13 21 34

def fib(n):
    now = 1
    ans = 1
    temp = 1

    if n < 3: return 1
    else:
        for i in range(3, n+1):
            ans = temp + now
            temp = now
            now = ans

    return ans


print(fib(11))
