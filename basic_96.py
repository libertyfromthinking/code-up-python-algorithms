num_mono = int(input("흰돌의 개수를 입력하시오 : "))
loc = [list(map(int, input("흰돌의 x,y 좌표를 입력하세요 : ").split())) for i in range(num_mono)]
l = [[0]*19 for i in range(19)]

for i in range(num_mono):
    x=0 
    y=0
    for j in range(2):
        if j==0:
            x = loc[i][j]-1
        else:
            y = loc[i][j]-1
    l[x][y] = 1

for i in l:
    print(' '.join(list(map(str,i))))
