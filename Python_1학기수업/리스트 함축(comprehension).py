# 리스트 함축(comprehension)

# 리스트
lst = [1, 2, 3, 4, 5]
print(lst)

print()

lst = [i**2 for i in lst]
print(lst)

print()

# 튜플
test = ("apple", "banana", "orange")
test_len = [len(i) for i in test]
print(test_len)

print()

# 딕셔너리
d = {100: "apple", 200: "banana", 300: "orange"}
d_upper = [v.upper() for v in d.values()]
print(d_upper)
