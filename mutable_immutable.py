# mutable : 변경되는 객체(객체의 상태를 변경할 수 있음)
# - 종류 : list, set, dictionary
# immutable : 변경되지 않는 객체(객체의 상태를 변경할 수 없음)
# - 종류 : int, float, str, boo, tuple

# immutable 객체 (상태 변경X)
# 5개 전부 주소가 같다
# 한 곳을 가리킨다
print("immutable 객체")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a))) # 0x2688e1a0d30
print(hex(id(b))) # 0x2688e1a0d30
print(hex(id(c))) # 0x2688e1a0d30
print(hex(id(d))) # 0x2688e1a0d30
print(hex(id(e))) # 0x2688e1a0d30

# mutable 객체 (상태 변경 O)
# 5개 전부 주소가 다르다
# 메모리가 각각 따로따로 잡힌다
print("\nmutable 객체")
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]
arr5 = [1, 2, 3]
print(hex(id(arr1))) # 0x2688e2f3e80
print(hex(id(arr2))) # 0x2688e2e3d00
print(hex(id(arr3))) # 0x2688e2f1a40
print(hex(id(arr4))) # 0x2688e2f1bc0
print(hex(id(arr5))) # 0x2688e2f1dc0

# immutable 객체 거의 대부분 같은 값을 참조한다 -> 같은 주소를 나타낸다
# 주소가 같으면 같은 값을 참조한다
# immutable 객체 - int 값 변경시
print("=" * 50)
print("immutable 객체 예제")
print("=" * 50)
num1 = 99
num2 = 99
num3 = 99
num4 = 99
print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num1 값 : {num3} \t주소 : {hex(id(num3))}")
print(f"num1 값 : {num4} \t주소 : {hex(id(num4))}")
num1 += 1 # num1 값 증가
num3 += 1 # num3 값 증가
num4 += 10 # num4 값 증가
print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4} \t주소 : {hex(id(num4))}")

# immutable 객체 - string 값 변경시
print("\n2. str 값이 변경되면?")
s1 = "BlockDMask"
s2 = "BlockDMask"
s3 = "BlockDMask"
s4 = "BlockDMask"
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s2} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s2} \t주소 : {hex(id(s4))}")
s1 = s1.replace('D', 'ZZZ') # replace로 값을 변경하고, 새로운 문자열을 s1에 대입하게 됨
s2 = "BlockZZZMask" # replace로 변경한 문자열과 동일한 문자열로 변경할 때
s4 = s3.upper() # s4를 대문자로 변경
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s2} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s2} \t주소 : {hex(id(s4))}")

# mutable 객체(상태 변경 가능) - list, set, dictionary
# 메모리에 각각 값들이 생성되고 참조를 각각 하기 때문에 다들 주소가 다르게 나온다.
# 내부의 값이 변한다 하더라고, 최초 참조 메모리 주소가 변경하지 않는다.
# 값을 바꾸면 값은 바뀌지만 주소값은 변하지 않는다
print("=" * 50)
print("mutable 객체 예제.")
print("=" * 50)
print("1. list 값이 변경되면?")
arr1 = ['a', 'b', 'c', 77]
arr2 = ['a', 'b', 'c', 77]
arr3 = ['a', 'b', 'c', 77]
print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr2 값 : {arr3} \t주소 : {hex(id(arr3))}")
arr1.append(10) # ['a', 'b', 'c',77, 10] 
arr2.append(10) # ['a', 'b', 'c',77, 10] 
print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr2 값 : {arr3} \t주소 : {hex(id(arr3))}")

# dictionary 객체
print("\n2. dictionary 값이 변경되면?")
d1 = {'a' : 11, 'b' : 22, 'c' : 33}
d2 = {'a' : 11, 'b' : 22, 'c' : 33}
d3 = {'a' : 11, 'b' : 22, 'c' : 33}
print(f"arr1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"arr2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"arr2 값 : {d3} \t주소 : {hex(id(d3))}")
d1['a'] = 99
d2['d'] = 44
print(f"arr1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"arr2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"arr2 값 : {d3} \t주소 : {hex(id(d3))}")

# 얕은 복사 깊은 복사를 하기 위해서 mutable, immutable을 사용함




