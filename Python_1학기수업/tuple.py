t = (1, 2, 3)
print(type(t)) # tuple

# 튜플(tuple)이 주로 사용되는 경우
# 함수에서 하나 이상의 값을 리턴하는 경우
def calc(a, b): # def 변수(): -> 함수
    return a+b, a*b

x, y = calc(5, 4)
print(x, y) # 9 20

# 문자열 포맷팅
print("id : %s, name : %s" % ("kim", "김유신")) # id : kim, name : 김유신

# 튜플에 있는 값을 함수 인수로 사용하는 경우
args = (3, 4)
print(calc(*args)) # 7 12