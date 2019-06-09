char_list = []

while 'q' not in char_list:
    char_list = input("영문자를 입력하세요. q가 나오면 종료됩니다 : ").split()
    for i in char_list:
        print(i)
        if i=='q':
            break
