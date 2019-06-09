while 1:
    s = int(input("10000이상 99999이하의 수를 입력하십시오 : "))
    multi = 10000
    
    #s = str(s)
    if 10000<=s and s<=99999:
        s = str(s)
        for i in range(len(s)):
            if s[i]:
                int_s = int(s[i])
                print(f'[{int_s*multi}]')
            multi = int(multi/10)
    else:
        print("올바른 범위의 값을 입력하세요 : ")
