i1, i2 = input("두 값의 bool값이 같을 때만 1 아닐 때는 0을 출력합니다 : ").split()
i1 = int(i1)
i2 = int(i2)

if bool(i1)==bool(i2):
    print(bool(1))
else:
    print(bool(0))

