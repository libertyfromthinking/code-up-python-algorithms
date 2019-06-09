i1, i2 = input("주사위 두개의 숫자를 입력하면 나올 수 있는 경우의 수를 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)

for i in range(1, i1+1):
    for j in range(1, i2+1):
        print(i,' ',j)

