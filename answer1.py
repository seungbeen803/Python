num = "881120-1068234"
print("연월일 : ", num[0:6])
print("숫자 : ", num[7:])

print("성별 : ", num[7])

# split
hong = "881120-1068234"
num = hong.split('-')
print("연월일 : ", num[0])
print("숫자 : ", num[1])

# 리스트
n = [1, 3, 5, 4, 2]
print("원본 : ", n)
n.sort() # 오름차순
n.reverse() # 거꾸로 정렬
print("결과 : ", n)

# join
li = ['Life', 'is', 'too', 'short']
str = " ".join(li)
print(str)

# for문
list1 = ['Life', 'is', 'too', 'short']
for i in list1:
    print(i, end = " ")

print()

# 튜플
t = (1, 2, 3)
t += (4,)
print(t)

# 다른 방법
t = (1, 2, 3)
u = 4,
print(t+u)

# 딕셔너리
a = {'A' : 90, 'B' : 80, 'C' : 70}
print("원본 딕셔너리 : ", a)
b = a.pop('B') # 여기 중요!!
print("'B' 추출 후 딕셔너리 : ", a)
print("추출된 B의 값 : " , b)

import copy
a = {'A' : 90, 'B' : 80, 'C' : 70}
a2 = copy.deepcopy()