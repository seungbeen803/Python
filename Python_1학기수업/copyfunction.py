# copy.copy(변수)
import copy
print("import copy")
print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = copy.copy(arr1) # 여기서 복사 copy 함수 이용

print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22) # arr2에 값 추가
print('arr2.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 딕셔너리
import copy # copy 모듈 불러오기
print('=' * 50)
d1 = {'a': 'Mirim', 'b' : [1, 2, 3]}
d2 = copy.copy(d1) # copu 모듈 얕은 복사
print("1. 전체 출력")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

print("\n2. 리스트의 끝에 값 추가")
d2['c'] = 'kimchi'
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

# 리스트 안에 있는 리스트
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 값 추가")
d1['b'].append('NO')
print("d1['b'].append('NO')")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n5. 리스트 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')