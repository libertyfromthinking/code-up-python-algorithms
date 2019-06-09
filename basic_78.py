i = int(input("1~100사이의 정수를 입력하면 입력된 수까지 짝수의 합을 출력합니다 : "))
result = 0

for j in range(i+1):
    result = result+j if j%2==0 else result

print(result)
