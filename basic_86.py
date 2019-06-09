w = int(input("가로 해상도를 입력하세요 : "))
h = int(input("세로 해상도를 입력하세요 : "))
b = int(input("비트수를 입력하세요 : "))

result = (w*h*b)/8388608

print(f'{w}*{h}크기에 {b}비트의 이미지를 저장하려면 {result:0.2f}MB의 저장공간이 필요합니다.')
