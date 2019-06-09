r = input("웹사이트에 가입한 인원 세명이 웹사이트에 방문하는 주기를 입력합니다 : ").split()
r1 = int(r[0])
r2 = int(r[1])
r3 = int(r[2])
day = int(max(r))
     
while day%r1!=0 or day%r2!=0 or day%r3!=0:
    day=day+1
else:
    print(day)
    
