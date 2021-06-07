# 각 자리수의 합을 도출해 내는 코드
# 인풋은 일련의 숫자로 입력이 됨
def sum_digits(n):
    num_list = list(str(n))  # 인풋을 리스트로 변경해줌

    if len(num_list) == 1:  # 리스트의 길이가 1이란 소리는 마지막 숫자란 소리니까 그냥 int n을 리턴
        return int(n)
    else:
        num = int(num_list.pop(0))  # 가장 첫번째 값을 int로 추출해내고
        pack = ''.join(num_list)    # 남은 리스트는 다시 하나의 숫자로 통일
        return num + sum_digits(pack)  #그리고 나서 첫번째 값인 num과 재귀함수를 써서 둘이 더해줌




print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))



# 아래는 모범 답안 코드
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10) # 1