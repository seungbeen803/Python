# 디폴트 값을 갖는 함수
def hello(msg="안녕하세요"):
    print(msg + "!")
hello("오랜만이에요")
hello("이영희")
hello()

def rolling_dice(pip=6, repeat=1):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)