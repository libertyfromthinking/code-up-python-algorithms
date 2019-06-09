num = int(input("출석번호를 부를 횟수를 입력하세요 : "))
attend_num = list(map(int,input("출석번호를 입력하세요 : ").split()))
l = [0]*23

for i in range(0,num):
    l[attend_num[i]]+=1

l = list(map(str,l))
print(' '.join(l))
