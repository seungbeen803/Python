# mutable 객체 -> 리스트, 딕셔너리는 mutable
print("=" * 50)
print("mutable 객체 요소로 존재하는 immutable, mutable")
print("=" * 50)
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']

# 리스트(immutable)  객체의 주소
# 리스트는  mutable이므로 주소값이 다르다
print(f"arr1 : {arr1} \t : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t : {hex(id(arr2))}")

# 리스트 내부의 mutable 요소
print("-" * 50)
print("리스트 내부의 mutable 요소들")
print(f"arr1[0] : {arr1[0]} \t 주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr2[0]} \t 주소 : {hex(id(arr2[0]))}")
print(f"arr1[1] : {arr1[1]} \t 주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr2[1]} \t 주소 : {hex(id(arr2[1]))}")
print(f"arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}")
print(f"arr1[4] : {arr1[4]} \t 주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr2[4]} \t 주소 : {hex(id(arr2[4]))}")

# 리스트 내부의 mutable 요소
print("-" * 50)
print('리스트 내부의 mutable 요소들')
print(f"arr1[2] : {arr1[2]} \t 주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t 주소 : {hex(id(arr1[2]))}")
# 리스트 내부에 있는 mutable 요소를 보면
# 각각 주소가 또 다른 것을 볼 수 있음