#  인자 전달
from glob import glob


g=1
def testScope(a):
    # 전역방 하나만 잡는다
    global g # 전역 변수 global이 있다면 지역 변수 g의 1이 아닌 전역 변수 2를 출력
    g=2
    return g+a
print(testScope(1))
print(g)