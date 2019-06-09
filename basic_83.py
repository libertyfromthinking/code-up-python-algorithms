i = int(input("1~10사이의 입력된 수까지 3, 6, 9는 X로, 나머지는 숫자로 출력합니다 : "))
l = []

for j in range(1,i+1):
    if str(j) =='3' or str(j)=='6' or str(j)=='9':
        l.append('X')
    else:
        l.append(str(j))

l = ' '.join(l)
print(l)


