# list(), set(), tuple()

a = set((1, 2, 3, 2)) # 중복된 것은 1개만 나온다 
print(a) # {1, 2, 3}
print(type(a)) # <class 'set'>

# set를 list로 바꿈
b = list(a)
print(b) # [1, 2, 3]
print(type(b)) # <class 'list'>

# list를 tuple로 바꿈
c = tuple(b)
print(c) # (1, 2, 3)
print(type(c)) # <class 'tuple'>