maze_arch = [[0]*10 for i in range(10)]
for i in range(10):
    maze_arch[i][0] = 1
    maze_arch[i][9] = 1
    if i==0 or i==9:
        for j in range(1,9):
            maze_arch[i][j]=1

n = int(input("벽의 개수를 입력하세요 : "))

for i in range(n):
    wall_x, wall_y = map(int,input("벽이 세워질 좌표를 입력하세요 : ").split())
    maze_arch[wall_y-1][wall_x-1] = 1

feed_x, feed_y = map(int, input("먹이의 위치를 입력하세요 : ").split())
maze_arch[feed_y-1][feed_x-1] = 2

feed = True
x = 1
y = 1

print('미로의 형태')
for i in maze_arch:
    print(' '.join(list(map(str,i))))

while feed:
    if maze_arch[y][x]==2:
        feed = False
        print('먹이를 찾았습니다')
    elif maze_arch[y][x+1]!=1 and x+1<10:
        maze_arch[y][x]=9
        x = x+1
        print('가로로 이동했습니다')
    elif maze_arch[y+1][x]!=1 and y+1<10:
        maze_arch[y][x]=9
        y = y+1
        print('세로로 이동했습니다')
    else:
        pass
    if x==8 and y==8:
        break
    #x=5 y=6

print('결과입니다')

for i in maze_arch:
    print(' '.join(list(map(str,i))))
