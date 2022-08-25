# 얕은 복사(Shallow Copy) : 주소가 복사되어 객체를 공유하는 얕은 복사(Shallow Copy)
# 복사를 했음에도, 값을 변경하면 다른 변수에도 영향을 끼치도록 '참조만'
# 얕은 복사 기호 -> "="
# 해당 객체들은 값이 변경되면 '무조건' 참조가 변경되기 때문에 얕은 복사를 해서 값을 변경하더라도, 참조하던 다른 객체의 값도 변경되거나 하지 않음
# list, set, dictionary
arr1 = [1, 2, 3]
arr2 = arr1
print(f'arr1 : {arr1} \t 주소 : {hex(id(arr1))}')
print(f'arr2 : {arr2} \t 주소 : {hex(id(arr2))}')

arr1.append(4)
print(f'arr1 : {arr1} \t 주소 : {hex(id(arr1))}')
print(f'arr2 : {arr2} \t 주소 : {hex(id(arr2))}')

# [:]을 이용한 얕은 복사
# "메모리 주소 다르니까 깊은 복사"
print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:] # 여기서 복사
print("1. 전체 출력")
print(f'arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22) # arr2에 값 추가
print('arr2.append(22)')
print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]} \t 주소, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t 주소, add : {hex(id(arr2[3]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f"arr1[3] : {arr1[3]} \t 주소, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t 주소, add : {hex(id(arr2[3]))}")

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1} \t 주소, add : {hex(id(arr1))}')
print(f'arr2 : {arr2} \t 주소, add : {hex(id(arr2))}')