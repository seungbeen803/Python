# 1. 튜플 생성
# 형식 : (값 1, 값 2, 값 3)

t = ()
print(t) # ()

xy = (2560, 1440)
print(xy) # (2560, 1440)

color = 129, 247,216

print(xy + color) # (2560, 1440, 129, 247, 216)
print(xy * 2) # (2560, 1440, 2560, 1440)

# 2. 패킹과 언패킹
color = 129, 247, 216
red, green, blue = color
print(red) # 129
print(green) # 247
print(blue) # 216

x, y = 1920, 1080
print(x) # 1920
print(y) # 1080

# 3. 튜플 활용
x = 2560
y = 1440
x, y = y, x # 직관적인 교환(swap)이 가능하다.
print(x) # 1440
print(y) # 2560

a = (123, "abc", True, 123)
print(a[1]) # 'abc'
print(a[2:]) # (True, 123)
print(a[:2]) # (123, 'abc')

# error가 생긴다 튜플은 값을 수정할 수 없다
# a[1] = 2
# print(a[1])

print(a.index("abc")) # 1
print(a.count(123)) # 2