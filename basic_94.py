num = int(input("출석번호를 부를 횟수를 입력하세요 : "))
attend_num = list(map(int,input("출석번호를 입력하세요 : ").split()))
l = []
for i in range(num):
    i = i*-1-1
    l.append(attend_num[i])

print(l)
