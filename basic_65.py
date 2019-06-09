il = input("세 개의 정수중 짝수만 출력합니다 : ").split()

for i in il:
    if int(i)%2==0:
        print(i)
