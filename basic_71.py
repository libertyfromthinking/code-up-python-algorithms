input_list = []

while '0' not in input_list:
    input_list = input("여러개의 정수를 입력하세요. 0이 발견되면 종료됩니다 : ").split()
    for i in input_list:
        print(i)
        if i=='0':
            break

