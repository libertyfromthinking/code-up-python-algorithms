i = int(input("1에서 입력된 정수까지 출력하되 3의 배수는 출력하지 않습니다 : "))

for j in range(1,i+1):
    if j%3==0:
        continue
    else:
        print(j)
