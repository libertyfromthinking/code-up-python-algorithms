i1, i2 = input("두 가지가 모두 참일 때 1, 아니면 0이 출력됩니다 : ").split()
i1 = int(i1)
i2 = int(i2)
if i1 and i2:
    print(bool(1))
else:
    print(bool(0))
