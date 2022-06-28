# break, continue문
# break문 : 반복을 즉시 멈추고, 반복문 밖으로 빠져나감
for i in range(1, 9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i, 2*i))

print()

for i in range(1, 9+1):
    if i == 7:
        continue
    print("2 x {} = {}".format(i, 2*i))

# continue : 다음 순서의 반복 시작점으로 제어가 이동
for i in range(1, 9+1):
    if i % 2 ==0:
        continue
    print("2 x {} = {}".format(i, 2*1))

print()

for i in range(1, 9+1):
    if i % 2 ==0:
        break
    print("2 x {} = {}".format(i, 2*1))

print()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lst:
    if item > 5: break
    print("itme:{0}".format(item))

print()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lst:
    if item % 2 == 0: continue
    print("itme:{0}".format(item))

# 좀 더 알아보기
array = []
for i in range(1, 10, 2): # (first, last, 증가값)
    print(array.append(i*i))

array = [i*i for i in range(1, 10, 2)]
print(array)

array = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array)