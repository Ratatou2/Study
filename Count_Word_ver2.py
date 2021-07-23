def count_word():
    count_dict = {}
    file = open("HarryPotter.txt", "r",  encoding='UTF8')
    lines = file.readlines()

    for line in lines:
        words = line.split(' ')
        for word in words:
            count_dict[word] = count_dict.get(word, 0) + 1

    big_word = None
    big_count = 0
    for word, count in count_dict.items():
        if count > big_count:
            big_word = word
            big_count = count

    print(big_word, big_count)


count_word()