i1, i2, i3 = input("물감의 종류 세가지 각각의 수를 입력하면 최대 개수를 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
cnt = 0

for i in range(i1):
    for j in range(i2):
        for k in range(i3):
            print(f'{i} {j} {k}')
            cnt = cnt+1

print(cnt)


