# 1. 튜플 생성
# 일반적인 경우에 데이터를 묶어서 한 번에 전달하거나 여러 개의 값을 묶어서 한 번에 반환할 경우에 사용됩니다.
t = ()
print(t) # ()

xy = (2560, 1440)
print(xy) # (2560, 1440)

color = 129, 247, 216
print(color) # (129, 247, 216)

print(xy + color)  # (2560, 1440, 129, 247, 216)
print(xy * 2) # (2560, 1440, 2560, 1440)

print()

# 2. 패킹과 언패킹
color = 129, 247, 216
red, green, blue = color

print(red) # 129
print(green) # 247
print(blue) # 216
x, y = 1920, 1080
print(x) # 1920
print(y) # 1080

print()

# 3. 튜플 활용 : 함수에서 하나 이상의 값을 리턴 하는 경우
x = 2500
y = 1440
x, y = y, x
print(x) # 1440
print(y) # 2500

a = (123, "abc", True, 123)
print(a[1]) # abc

print(a[2:]) # (True, 123)
print(a[:2]) # (123, 'abc')

# 튜플은 값을 수정할 수 없기 때문에 값을 수정할 시 에러가 발생한다.
# a[1] = 2
# print(a[1])

print(a.index("abc")) # 1
print(a.count(123)) # 2

t = (1, 2, 3)
print(t) # (1, 2, 3)
t += (4,) # (1, 2, 3, 4)
print(t)

