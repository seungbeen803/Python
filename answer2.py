#set
# 리스트에서 중복된 숫자들을 제거해보기
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
print("원본 : ", a)
a = set([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5])
b = list(a)
print("중복제거 후 : ", b)

# 변수
# 1번 인덱스인 2가 사라지고 4가 들어간다
a=b=[1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))
a[1]=4
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

