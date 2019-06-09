a, d, n = input("등차수열의 시작값, 등차의 값, 몇번째 인지를 나타내는 정수를 입력하십시오 : ").split()
a = int(a)
d = int(d)
n = int(n)

for i in range(2,n+1):
    a = a+d
else:
    print(a)
