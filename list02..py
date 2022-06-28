# 1. 리스트 생성
from audioop import reverse


l = []
player = ["Messi", 10, True]
print(list("Happy")) # ['H', 'a', 'p', 'p', 'y']
print(list((1225, 2436))) # [1225, 2436] , tuple -> list로 바꿔준다
print(list({"menu":"pizza", "price":10000})) # ['menu', 'price'], dictionary -> list로 바꿔준다
print(list({"사과", "배"})) # ['사과', '배']
nums = list(range(3)) # [0, 1, 2]

print()

# 2. 리스트에 요소 추가
nums + [10, 11]
print(nums) # [0, 1, 2, 10, 11]
print(nums + [10, 11]) # [0, 1, 2, 10, 11]

nums += [10, 11]
print(nums) # [0, 1, 2, 10, 11]

# 맨 뒤에 20 추가
nums.append(20)
print(nums) # [0, 1, 2, 10, 11, 20]

# list 추가
nums.append([30, 31]) 
print(nums) # [0, 1, 2, 10, 11, 20, [30, 31]]

# 인덱스 2번 자리에 40 추가
nums.insert(2, 40)
print(nums) # [0, 1, 40, 2, 10, 11, 20, [30, 31]]

# 값으로 만 들어간다.
nums.extend([50, 51]) 
print(nums) # [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]

# 3. 리스트에 요소 수정
# 인덱스 7번 출력
print(nums[7]) # [30, 31]

# 인덱스 7번 자리에 60 추가
nums[7] = 60
print(nums) # [0, 1, 40, 2, 10, 11, 20, 60, 50, 51]

print()

# 4. 리스트에서 요소 제거
# 어떤 위치 삭제
print(nums) # [0, 1, 40, 2, 10, 11, 20, 60, 50, 51]
del nums[2] 
print(nums) # [0, 1, 2, 10, 11, 20, 60, 50, 51]
# 해당 값 삭제
nums.remove(20)
print(nums) # [0, 1, 2, 10, 11, 60, 50, 51]

# 맨 마지막 데이터(값) 삭제
nums.pop()
print(nums) # [0, 1, 2, 10, 11, 60, 50]

nums.pop(5)
print(nums) # [0, 1, 2, 10, 11, 50]

nums.append(10)
print(nums) # [0, 1, 2, 10, 11, 50, 10]

# remove 했을 때 중복 된 값이 있으면 앞에서부터 삭제 된다.
nums.remove(10)
print(nums)

# 모든 요소 삭제
nums.clear()
print(nums) # []

print()

# 5. 리스트에서 요소 검색
nums = list(range(3))
print(nums) # [0, 1, 2]

nums += [100, 10]
print(nums) # [0, 1, 2, 100, 10]

nums[3]
print(nums) # [0, 1, 2, 100, 10]

# 값 in 리스트 : 리스트에 값이 있는지 확인한다.
# nums 안에 3이 들어 있는가
print(3 in nums) # False

# nums 안에 10이 들어 있는가
print(10 in nums) # True

print()

# 6. 기타 리스트 관련 함수
len(nums)
print(nums)

# 오름차순
nums.sort()
print(nums)

# 거꾸로 정렬
# sort하고 reverse를 하면 내림차순이 된다
nums.reverse()
print(nums)

# range() 함수 50p