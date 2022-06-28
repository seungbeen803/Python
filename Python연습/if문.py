# 1. 기본 if문
# 형식
# if 조건식:
#     명령어1
#     ...
# else:
#     명령어2
#     ...

x = int(input())

if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

password = input()
if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다")