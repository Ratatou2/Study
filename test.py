# 잔돈 계산기
# 나머지를 구하고 원하는 값으로 나누면 코드를 더 간략화 시킬수 있음
# 이게 가능한 이유는 앞서 구한 5만원과 1만원들이 각각 5000과 1000의 배수라서 그럼
# 그러니까 4만원짜리 돈이 있었다면 이렇겐 못했겠지

def calculate_change(payment, cost):
    rest = payment - cost

    fif_thou = rest // 50000
    ten_thou = (rest % 50000) // 10000
    fiv_thou = (rest % 10000) // 5000
    one_thou = (rest % 5000) // 1000

    print("50000원 지폐: {}장".format(fif_thou))
    print("10000원 지폐: {}장".format(ten_thou))
    print("5000원 지폐: {}장".format(fiv_thou))
    print("1000원 지폐: {}장".format(one_thou))

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)