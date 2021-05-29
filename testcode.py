import random


word_list = []

with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        word_list.append(line.strip().split(": "))

while True:
    random_int = random.randint(0, 7)
    print(f"{word_list[random_int][1]}")
    user_input = input()

    if user_input == 'q': break
    elif user_input == word_list[random_int][0]:
        print("맞았습니다")
    else:
        print(f"아쉽습니다. 정답은 {word_list[random_int][0]}입니다.")

