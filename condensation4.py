def mask_security_number(security_number):
    # rebuild = []
    # for i in range(len(security_number)):
    #     rebuild.append(security_number[i])
    #문자열을 리스트로 만들떈 이렇게 안하고 rebuild = list(security_number) 라고 해도 충분함... 멍충쓰...

    rebuild = list(security_number)

    for i in range(1, 5):
        rebuild[-i] = "*"

    sum = str()
    for i in rebuild:
        sum += i

    return sum



# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))