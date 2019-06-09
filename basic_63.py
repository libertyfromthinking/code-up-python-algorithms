i1, i2 = input("두 개의 정수중 조건문 없이 큰값을 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)
result = i1>i2 and i1 or i2

print(f'{result}')

