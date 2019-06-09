i1, i2, i3 = input("세 개의 정수중 조건문 없이 작은값을 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)

result = bool(i1==0 or i2==0 or i3 ==0) and str(0) or (i1>i2 and i2 or i1)
result = type(result)!=int and str(0) or (result>i3 and i3 or result)
print(f'{result}')

