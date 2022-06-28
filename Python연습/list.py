# 1. 리스트 생성
# 형식 : [값 1, 값 2, 값 3]

l = []
player = ["Messi", 10, True]
print(player) # ['Messi', 10, True] 
print(list("Happy")) # ['H', 'a', 'p', 'p', 'y']
print(list((1125, 2436))) # [1125, 2436]
print(list({"menu":"pizza","price":10000})) # ['menu', 'price']
print(list({"사과", "배"})) # ['사과', '배']
nums = list(range(3))
print(nums) # [0, 1, 2]

# 2. 리스트에 요소 추가
nums = list(range(3))
print(nums) # [0, 1, 2]

print(nums + [10, 11]) # [0, 1, 2, 10, 11]
nums += [10, 11]
print(nums) # [0, 1, 2, 10, 11]

# append() : 인자가 리스트면 그 리스트를 한 요소로 추가한다
nums.append(20)
print(nums) # [0, 1, 2, 10, 11, 20]
nums.append([30, 31])
print(nums) # [0, 1, 2, 10, 11, 20, [30, 31]]

# insert() : 인덱스 위치에 값을 요소로 추가한다
nums.insert(2, 40)
print(nums) # [0, 1, 40, 2, 10, 11, 20, [30, 31]]

# extend() : 인자가 리스트면 리스트를 해제하여 하나씩 요소를 추가한다
nums.extend([50,51])
print(nums) # [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]

# 3. 리스트에 요소 수정
print(nums[7]) # [30, 31]
nums[7] = 60
print(nums) # [0, 1, 40, 2, 10, 11, 20, 60, 50, 51]

# 4. 리스트에서 요소 제거
del nums[2]
print(nums) # [0, 1, 2, 10, 11, 20, 60, 50, 51]

nums.remove(20)
print(nums) # [0, 1, 2, 10, 11, 60, 50, 51]

nums.pop()
print(nums) # [0, 1, 2, 10, 11, 60, 50]

nums.pop(5)
print(nums) # [0, 1, 2, 10, 11, 50]

nums.clear()
print(nums) # []

# 5. 리스트에서 요소 검색
nums = list(range(3))
print(nums) # [0, 1, 2]

nums += [100, 10]
print(nums) # [0, 1, 2, 100, 10]
print(nums[3]) # 100

# 값 in 리스트 : 리스트에 값이 있는지 확인
print(3 in nums) # False
print(10 in nums) # True

# 6. 기타 리스트 관련 함수
# len(리스트) : 리스트의 각 요소의 개수를 센다
print(len(nums)) # 5

# 오름차순
nums.sort()
print(nums) # [0, 1, 2, 10, 100]

# 내림차순
nums.reverse()
print(nums) # [100, 10, 2, 1, 0]