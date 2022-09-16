# main_exit.py
# 이 방식으로 임포트할 경우 해당 함수가 최상위 레벨 심볼로 등록되기 때문에 모듈명을 통하지 않고 바로 함수 호출 가능
# 많이 가져올 때, 앞에 이름. 쓰기 싫을 때
from sys import *
while True:
    print( "종료하려면 exit를 입력하세요" )
    user_input = input(">")
    if user_input == "exit":
        exit()