# 2. if ~ elif ~ else문
# 형식
# if 조건식 1:
#     코드 블록 1
# elif 조건식 2:
#     코드 블록 2
# elif 조건식 3:
#     코드 블록 3
# else:
#     코드 블록 4

x = int(input())

if x % 4 == 0:
    print("4의 배수")
elif x % 3 == 0:
    print("3의 배수")
elif x % 2 == 0:
    print("2의 배수")

x = int(input())

if 10 <= x < 20:
    print("10대")
elif 30 <= x < 40:
    print("30대")
else:
    print("10, 30대가 아님")