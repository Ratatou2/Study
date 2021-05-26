# 잔돈 계산기

def calculate_change(payment, cost):
    rest = payment - cost

    fif_thou = rest // 50000
    rest = rest - fif_thou * 50000

    ten_thou = rest // 10000
    rest = rest - ten_thou * 10000

    fiv_thou = rest // 5000
    rest = rest - fiv_thou * 5000

    one_thou = rest // 1000
    rest = rest - one_thou * 1000

    print("50000원 지폐: {}장".format(fif_thou))
    print("10000원 지폐: {}장".format(ten_thou))
    print("5000원 지폐: {}장".format(fiv_thou))
    print("1000원 지폐: {}장".format(one_thou))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)