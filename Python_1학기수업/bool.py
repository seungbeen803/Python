# 참과 거짓을 나타내는 자료형
# 사용 가능한 값은 True, False
# 수치를 논리연산자에 사용하는 경우
# - 0은 False로 간주
# 음수를 포함한 다른 값은 모두 True로 간주
# 문자열을 논리연산자에 사용하는 경우에도 "만 False로 간주
# 값이 없는 상태를 나타내는 None도 False 간주


isRight = False
print(type(isRight))
print(1 < 2) # True
print(1 != 2) # True
print(1 == 2) # False
print(True and True and True)
print(False or False or False)

print()

print(bool(0))
print(bool(-1))
print(bool("test"))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool(''))
print(bool(' '))

