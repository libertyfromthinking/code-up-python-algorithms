num = int(input("출석번호를 부를 횟수를 입력하세요 : "))
attend_num = list(map(int,input("출석번호를 입력하세요 : ").split()))
min = 24

for i in range(num):
    if min>attend_num[i]:
        min = attend_num[i]

print(min)

