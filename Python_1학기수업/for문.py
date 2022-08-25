# 기본적인 for문
# 이터레이션이 가능한 객체를 순차적으로 순회
# 데이터를 모아 놓은 지료형에서 각 요소를 꺼내어 반복하는 형식으로 구현
# 형식 for <target> in <object>:

# 기본적인 for 문의 예 - 응용
# 리스트
lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

# 딕셔너리
d = {"apple": 100, "oramge": 200, "banana": 300}
for k, v in d.items(): # d.items는 items를 모두 가져오겠다는 의미(딕셔너리만 사용)
    print(k, v)

# 튜플
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# 별 찍기
for i in [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10] :
    print("*"*i)

# print()
# for i in range(1, 11) :
#     print("*"*i)

for i in range(1, 10+1): # 10이면 1~9까지 반복되는데 +1을 해줘야 10번 반복한다
    for j in range(1, i+1) :
        print("*", end="")
    print()

# 구구단
for i in range(1, 9+1) :
    print("2 x {} = {}".format(i, 2*i))
for i in range(1, 9+1) :
    print("3 x {} = {}".format(i, 3*i))
for i in range(1, 9+1) :
    print("4 x {} = {}".format(i, 4*i))
for i in range(1, 9+1) :
    print("5 x {} = {}".format(i, 5*i))

for dan in range(2, 5+1) :
    for i in range(1, 9+1) :
        print("{} x {} = {}".format(dan, i, dan*i))
    print()

# 피라미드 별 찍기
for i in range(1, 5+1) :
    print("  "*(5-i), "* "*(2*i-1))

