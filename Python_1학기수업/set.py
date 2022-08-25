# 세트(set) : 수학 시간에 배운 집합과 동일
# 유일한 값의 모임이며 순서는 없다.
a = {1, 2, 3, 4}
b = {3, 4, 4, 5}
print(a)
print(b)
print(type(a))
print(type(b))

print(a.union(b)) # {1, 2, 3, 4, 5}, 합
print(a.intersection(b)) # {3, 4}, 교
print(a.difference(b)) # {1, 2}, 차

# 기호
print(a | b) # {1, 2, 3, 4, 5}
print(a & b) # {3, 4}
print(a - b) # {1, 2}