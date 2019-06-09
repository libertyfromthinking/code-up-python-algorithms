i = int(input("합이 입력한 값보다 같거나 커지는 시점의 값을 출력합니다 : "))
result = 0

for j in range(1001):
    result = result+j
    if result>=i:
        print(j)
        break

