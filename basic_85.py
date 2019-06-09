h, b, c, s = input("소리 데이터 네가지를 입력하면 MB단위로 바꾸어 출력합니다 : ").split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

result = (h*b*c*s)/8388608
print(f'{result:0.1f}MB')

