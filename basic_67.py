i = int(input("정수 한개가 입력되었을 때 음수/양수, 홀수/짝수를 출력합니다 : "))
if i==0:
    print('this number is zero')
else:
    sign = 'plus' if i>0 else 'minus'
    oe = 'odd' if i%2 else 'even'
    print(f'{sign}\n{oe}')
