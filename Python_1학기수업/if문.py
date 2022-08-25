# 1. 기본 if문

a = 5
if(a>5):
    print("테스트 입니다.")
    print("a는 10입니다.")
else:
    print("else문 입니다.")

x = int(input())
print(x)
print(type(x))

# 짝수인지 홀수인지 출력
x = int(input("숫자 입력 : "))
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

print()

# 암호
password = input("password 입력 : ")
if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다.")