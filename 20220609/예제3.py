money = int(input("현 연봉을 입력하세요 : "))
test = str(input("근무평가등급을 입력하세요 : "))

if test == "우수":
   up =  money * 0.06
elif test == "보통":
    up =  money * 0.04
elif test == "불량":
    up = money * 0.02
print("연봉인상액 : ", int(up))
print("새 연봉인상액 : ", int(money+up))