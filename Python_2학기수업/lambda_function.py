# 람다 함수(lambda function)
# - 이름이 없고 함수 객체만 존재하는 익명 함수
# - 간단한 함수라면 람다를 사용하는 것이 편리할 때가 있음
# - 하나 정의해서 계속 사용할 정도는 아님

g = lambda x, y : x * y
print(g(2, 3))
print(g(3, 4))

print((lambda x : x * x)(3))
print(globals()) # lambda 함수라는 것을 알려준다