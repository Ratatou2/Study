def fib_tab(n):
    fib_dic = {1:1,
               2:1}

    if n in fib_dic:
        return fib_dic[n]

    elif n < 3:
        fib_dic[n] = 1

    else:
        for i in range(3, n+1):
            fib_dic[i] = fib_dic[i-2] + fib_dic[i-1]
            print(i, fib_dic[i])

    return fib_dic[n]

# 테스트
print(fib_tab(16))
print(fib_tab(53))
print(fib_tab(132))

'''
해답
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
'''