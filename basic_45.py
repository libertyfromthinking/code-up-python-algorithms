i1, i2 = input("값을 두개 입력하면 합, 차, 곱, 몫, 나머지, 몫+나머지를 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)
if i1<i2:
    i1, i2 = i2, i1

print(f'{i1+i2}\n{i1-i2}\n{i1*i2}\n{i1//i2}\n{i1%i2}\n{i1/i2}\n')

