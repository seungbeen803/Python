# 변수와 함수
# 프로그래밍 작업을 할 때 기본적으로 변수와 함수 필요
# 변수 : 여러 가지 값으로 변할 수 있는 수를 변수라고 한다.
# 프로그램을 작성하면서 변수에는 임의의 값을 담거나 함수가 리턴하는 값을 저장
# 함수 종류
# 필요한 기능이 미리 구현되어 있는 빌트인 함수
# 사용자가 직접 정의한 함수

# 변수
strA = "Hello python"
x = 5
y = 3.14
print(type(strA)) # <class 'str'>
print(type(x))    # <class 'int'>
print(type(y))    # <class 'float'>

# 함수
import keyword
print(keyword.kwlist) # 파이썬 키워드

# 문자열을 결합할 때 더하기 연산자는 생략 가능
print("py""thon")  # python
print("py"+"thon") # python

# *를 통해 반복 가능
print("py"*3)     # pypypy

# 문자열 인덱싱
strA = "python"
print(strA[0])   # p 

# 문자열 슬라이싱
strA = "python"
print(strA[0:1])  # p
print(strA[1:3])  # p
print(strA[:2])   # yt
print(strA[-2:])  # on
print(strA[:])    # python

strB = "python is powerful"
print(strB[-1])   # l
print(strB[-2])   # u
print(strB[-3])   # f
print(strB[-8:])  # powerful
print(strB[7:18]) # is powerful
print(strB[:])    # python is powerful
print(strB[::2])  # pto spwru 두 칸씩 띄워서
print(strB[-11:-9]) # is
print(strB[-18:-12]) # python


