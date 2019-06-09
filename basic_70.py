month = int(input("해당월을 입력하면 계절이 출력됩니다 : "))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

if month in winter:
    print('winter')
elif month in spring:
    print('spring')
elif month in summer:
    print('summer')
elif month in fall:
    print('fall')
