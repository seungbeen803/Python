num = int(input("수 입력 : "))

if num % 3 == 0:
    print(num, "은(는) 3의 배수이다.")
if num % 5 == 0:
    print(num, "은(는) 5의 배수이다.")
if num % 8 == 0:
    print(num, "은(는) 8의 배수이다.")
# 아니고 : and
# and의 not은 or
if num % 3 == 0 and num % 5 == 0 and num % 8 == 0:
    print(num, "어느 배수도 아니다.")