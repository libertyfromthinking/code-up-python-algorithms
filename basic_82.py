x = input("A~F 사이의 알파벳을 입력하면 16진수 구구단을 출력합니다 : ")
a = None

if x=='A':
    a = 10
elif x=='B':
    a = 11
elif x=='C':
    a = 12
elif x=='D':
    a = 13
elif x=='E':
    a = 14
elif x=='F':
    a = 15

for i in range(1,16):
    print(f'{x}*{i:#x}={a*i:#x}')





