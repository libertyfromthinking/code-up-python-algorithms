while 1:
    d = input("년월일을 입력하세요 (yyyy.mm.dd): ")
    y, m, d = d.split(".",3)
    if len(y)!=4 or len(m)!=2 or len(d)!=2:
        print("올바른 양식으로 입력하세요")
    else:
        print(f'{d}-{m}-{y}')

