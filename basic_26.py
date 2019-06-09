t = input("시간을 입력하세요 : ")
h, m,s = t.split(":",3)

if int(m)<10 and len(m)>1:
    print(f'{m[1]}')
else:
    print(f'{m}')


