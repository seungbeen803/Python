# 반복문 작성 시 도움이 되는 함수
# 형식) filter(<function> | None, <이터레이션이 가능한 자료형>)
# 앞에 함수 이름을 주거나, 함수가 필요없으면 None

# None을 쓰면 단순 반복
lst = [10, 25, 30]
itel = filter(None, lst)
for item in lst:
    print("item:{0}".format(item))

print()

# 함수 정의 def 함수이름(매개변수)
def getBiggerThan20(i):
    return i > 20 # return 값이 참이면 실행한다.

lst = [10, 25, 30]
itel = filter(getBiggerThan20, lst)
for item in itel:
    print("item: {}".format(item))