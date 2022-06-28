age = 18
print(age)

after_2 = 2
print(age + after_2)

result = age - after_2
print(result)

age = 18
print(age) # 18
age += 2
print(age) # 20
age -= 1
print(age) # 19
age *= 2
print(age) # 38
#age /= 2
#print(age) # 19.0
age //= 2 
print(age) # 9.0
age %= 6
print(age) # 3.0
age **= 3
print(age) # 27.0

# 자료형의 알려줌
age = 18
print(type(age))

pi = 3.14
print(type(pi))

age /= 2
print(type(age)) # 9.0

x = 10 + 3.14 
print(type(x)) # 13.14

# 여러 가지 진수
print(0b1100111000) # 2진수
print(0o130) # 8진수
print(0xD7A) # 16진수

print(type(0b1100111000))
print(type(0x130))
print(type(0xD7A))

# 지수 표현
print(10e3) # 10000.0
print(type(10e3)) # <class 'float'>

print(1.23456E2) # 123.456
print(type(1.23455E2)) # <class 'float'>

print(1.23456e-2) # 0.0123456
print(1.23456e22) # 1.23456e+22

# 복소수
print(8+24j) # (8+24j)

c = 1.2+3.4J 
print(type(1.2+3.4J)) # <class 'complex'>

print(c.real) # 1.2
print(c.imag) # 3.4
print(c.conjugate()) # (1.2-3.4j)

d = 1j
print(d * d.conjugate()) # (1+0j)

# 문자열
greeting = 'Hello'
to = "world!"
print(greeting) # Hello
print(type(greeting)) # <class 'str'>

say_hello = greeting + ", " + to 
print(say_hello) # Hello, world!

print("Hello"*5) # HelloHelloHelloHelloHello
print("\"Hello\"\n"+to) # "Hello"
                        # world!
multiline = """Happy
Programming"""
print(multiline) # Happy
                 # Programming
