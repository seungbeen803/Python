# 자신이 main 모듈
# 3단
def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1,10):
        print(n, "x", i, "=", n * i)

if __name__ == "__main__":
    gugudan(3)
print(__name__)