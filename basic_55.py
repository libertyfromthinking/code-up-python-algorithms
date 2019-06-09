i1, i2 = input("두 가지중 하나라도 참이면 1, 아니면 0이 출력됩니다 : ").split()
i1 = int(i1)
i2 = int(i2)
if i1 or i2:
    print(bool(1))
else:
    print(bool(0))
