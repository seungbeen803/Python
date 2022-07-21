# return

def swap(x, y):
    return y, x
print(swap(1, 2)) # 튜플 형태로 리턴 된다
retValue = swap(1,2)
print(retValue[0], retValue[1])

# 리턴 된 값은 튜플로 받는다
# 튜플은 함수도 별로 없고 값도 수정할 수 없다

# 하나의 값을 리턴하는 함수
def sum(*num):
    sum_value = 0 # 초기화는 무조건 해줘야한다(누적은 초기값을 줘야한다)
    for n in num:
        sum_value += n
    return sum_value
result=sum(1, 3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))

def min(*num):
    min_value = num[0]
    for n in num:
        if min_value > n:
            min_value = n
    return min_value
result=min(1, 3)
print("min(1, 3) =", result)
print("min(0, 3, -11) =", min(0, 3, -11))

import random

def dice(pip):
    result = random.randint(1, pip)
    return result
print("6면 주사위의 값은 :", dice(6))


# 리스트를 사용해 여러 값을 하나로 묶어 리턴하기
def multi_num(multi, star, end):
    result = []
    for n in range(star, end):
        if n % multi == 0:
            result.append(n)
    return result
multi2=multi_num(17, 1, 200)
print("multi_num(17, 1, 200) :", multi2)
print()
multi3=multi_num(3, 1, 100)
print("multi_num(3, 1, 100) :", multi3)

# 튜플을 사용해 여러 값을 여러 개 리턴하기
def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    return min, max
print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max((52, -3, 23, 89, -21))
print("최젓값:", min_value)
print("최곳값:", max_value)

def div_name(name):
    return name[0], name[1:]
sur_name, name = div_name("최승빈")
print("성:", sur_name, "이름:", name)