a, m, d, n = input("시작값, 곱할값, 더할값, 몇번째 인지를 나타내는 정수를 입력하십시오(a, m, d는 -50~50, n은 10이하의 자연수) : ").split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(2,n+1):
    a = a*m+d
else:
    print(a)
