i = int(input("1~1000까지 더해갈 때, 입력된 정수보다 같거나 큰 시점의 합을 출력합니다 : "))
result = 0

for j in range(1,1001):
    result += j
    if result>=i:
        print(result)
        break


