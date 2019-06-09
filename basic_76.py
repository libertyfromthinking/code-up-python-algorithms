c = ord(input("영문자가 입력되면 그 문자까지의 알파벳을 순서대로 출력합니다 : "))

alphabet = 97
print(chr(alphabet))

while alphabet!=c:
    alphabet = alphabet+1
    print(chr(alphabet))
