# 1. 정수형

# 덧셈
print(8 + 5) # 13

# 뺄셈
print(8 - 5) # 3

# 곱셈
print(8 * 5) # 40

# 나눗셈
print(8 / 5) # 1.6
# 산수적으로 소수점 아래까지 나옴

# 나눗셈의 몫 구하기
print(8 // 5) # 1

# 나눗셈의 나머지 구하기
print(8 % 5) # 3

# 거듭제곱
print(8 ** 5) # 32768

age = 18
print(age) # 18

after_2 = 2
print(age + after_2) # 20

result = age - after_2
print(result) # 16

age = 18
print(age) # 18
age += 2
print(age) # 20
age -= 1
print(age) # 19
age *= 2
print(age) # 38
age /= 2
print(age) # 19.0
age //= 2
print(age) # 9.0
age %= 6
print(age) # 3.0
age **= 3
print(age) # 27.0

# 2. 실수형
age = 18
print(type(age)) # <class 'int'>

pi = 3.14
print(type(pi)) # <class 'float'>

age /= 2
print(type(age)) # <class 'float'> # 9.0

x = 10 + 3.14
print(type(x)) # <class 'float'> # 13.14

# 3. 그 밖의 숫자 표현
# 가. 여러 가지 진수
print(0b1100111000) # 824 2진수

print(0o130) # 88 # 8진수

print(0xD7A) # 3450 # 16진수

print((0b1100111000)) # <class 'int'>

# 나. 지수 표현
# 지수 표현 e 뒤의 숫자는 x10^숫자를 뜻한다.
print(10e3) # 10000.0 = 10 x 10^3
print(type(10e3)) # <class 'float'>

print(1.23456E2) # 123.456 = 1.23456E2 x 10^2
print(type(1.23456E2)) # <class 'float'>

print(1.23456e-2) # 0.0123456 = 1.23456 x 10^-2
print(type(1.23456e-2)) # <class 'float'>

print(1.23456e22) # 1.23456e+22 = 1.23456 x 10^22

# 다. 복소수
# 파이썬에서 복소수는 j 또는 J를 사용한다.
print(8+24j) # (8+24j)

c = 1.2 + 3.4j
print(type(1.2 + 3.4j)) # <class 'complex'>

# 실수
print(c.real) # 1.2

# 허수
print(c.imag) # 3.4

# 복소수
print(c.conjugate()) # (1.2-3.4j)

d = 1j
print(d * d.conjugate()) # (1+0j)

# 라. 변환 함수
print(int(12.7)) # 12, 실수를 정수로 변환
print(int('321')) # 321,  문자열을 정수로 변환
print(float(456)) # 456.0, 정수를 실수로 변환
print(float('65.4')) # 65.4, 문자열을 실수로 변환
print(float('123e4')) # 1230000.0, 지수 표현을 실수로 표현
print(complex(1.23)) # (1.23+0j), 실수를 복소수로 표현
print(complex('1.23+45.6j')) # (1.23+45.6j), 문자열을 복소수로 표현
print(str(1.23)) # '1.23', 실수를 문자열로 변환

