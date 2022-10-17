# 06. datetime 클래스를 이용하여 오늘 날짜와 현재 시각을 구하고 weekday 메서드를 이용하여 오늘 날짜와 요일 정보를 출력하시오.
from datetime import datetime

today = datetime.today()
weekday = today.weekday()
week = ""
if weekday == 0:
    week = "월"
elif weekday == 1:
    week = "화"
elif weekday == 2:
    week = "수"
elif weekday == 3:
    week = "목"
elif weekday == 4:
    week = "금"
elif weekday == 5:
    week = "토"
else:
    week = "일"

result_format = "오늘은 {:d}년 {:d}일 {}요일 입니다."
result = result_format.format(today.year, today.month, today.day, week)
print(result)