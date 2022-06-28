# 함수 정의와 호출
# 매개 변수가 없는 함수
import random

# 처음 시작
n = random.randint(1, 6)
print("결과 : ", n)
n = random.randint(1, 6)
print("결과 : ", n)
n = random.randint(1, 6)
print("결과 : ", n)

# 함수화
def rolling_dice():
    n = random.randint(1, 6)
    print("6면 주사위 결과 : ", n)
rolling_dice()
rolling_dice()
rolling_dice()

def star():
    print("*****")
star()
star()
star()