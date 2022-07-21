def fn(a, b, c, *d):
    print(a, b, c, d)

# 다음 코드 모두 실행되지 않음
# fn(c=3, b=2, a=1, 4, 5)
# print(fn)
# fn(1, 2, c=3, 4, 5)
# print(fn)
# fn(4, 5, c=3, b=2, a=1)
