# 1. 비교 연산자
# 0이 아닌 모든 숫자는 True, 문자열에 문자가 하나라도 들어가면 True
a = 8
b = 3
print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a >= b) # True
print(a < b) # False
print(a <= b) # False

print()

# 2. 논리 연산자
print(not True) # False
print(not False) # True
print(False and False) # False
print(False and True) # False
print(True and False) # False
print(True and True) # True
print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True

print()

# 3. 비트 연산자
print(bin(0b1010)) # 0b1010
print(bin(0b1010 & 0b0110)) # 0b10
print(bin(0b1010 | 0b0110)) # 0b1110
print(bin(0b1010 ^ 0b0110)) # 0b1100
print(bin(~0b1010)) # -0b1011
print(~0b1010) # -11
print(bin(0b1010 << 2)) # 0b101000
print(0b1010 << 2 ) # 40
print(bin(0b1010 >> 2)) # 0b10
print(0b1010 >> 2 ) # 2