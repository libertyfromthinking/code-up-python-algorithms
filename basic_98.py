# 1. 첫째줄에 격자 가로 세로
# 2. 둘째줄에 막대 갯수
# 3. 셋째줄부터 막대 길이 방향 x y

w, h = map(int, input("격자의 가로 세로 크기를 입력하세요 : ").split())
n = int(input("막대 개수를 입력하세요 : "))
stick_list = [[0]*w for i in range(h)]

for i in range(n):
    l, d, x, y = map(int,input("막대의 길이, 방향, 좌표를 입력하세요 : ").split())
    x = x-1
    y = y-1
    for j in range(l):
        if d==0:
            stick_list[x][y+j] = 1
        else:
            stick_list[x+j][y] = 1

for i in stick_list:
    print(' '.join(list(map(str,i))))
