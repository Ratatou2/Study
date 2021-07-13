# txt파일 안에서 제일 많이 사용된 단어를 count하는 함수
def max_word():
    count_dict = {}  # 단어를 세줄 딕셔너리 생성
    file = open("CountWord.txt", 'r')  # 파일읽어오기
    lines = file.readlines()  # 모든 줄을 리스트안에 넣어옴, 추후에 for문을 쓰기 위함
    
    for line in lines:  # 한줄씩 가져옴
        reform = line.strip().split(' ') 
        for word in reform:  # 한줄씩 자른 문단에서 단어를 뽑아오는 작업
            word = word.strip('.?!').strip()
            if word == '':  # 단어가 공백이면 count 안함
                continue

            elif word not in count_dict:  # 공백이 아닌데 count_dict에 해당 단어가 없으면 추가해줌
                count_dict[word] = 1
 
            elif word in count_dict:  # 단어가 이미 있는 경우 value()를 +1
                count_dict[word] = count_dict[word] + 1

    best_count = max(count_dict.values())  # 값(value)중에 가장 큰 값을 찾음

    for word, count in count_dict.items():  # 값(value)로 키를 찾기 위한 for문
        if count == best_count:
            print(f'{word}가 총 {best_count}번 나왔습니다')

    file.close()


max_word()