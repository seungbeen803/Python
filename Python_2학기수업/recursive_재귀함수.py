# 재귀 함수(recursive)
# 재귀적인(recursive) 함수 호출은 함수 내부에서 자기 자신을 호출하는 것을 의미

# recursive
def factorial(x):
    if x==1:
        return 1
    return x * factorial(x-1)

print(factorial(3))