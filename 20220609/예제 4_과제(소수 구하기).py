# # 소수
num = int(input("수 입력 : "))

if num == 1: print("{}은 소수가 아니다".format(num)) # 1은 소수가 아님

for i in range(2, num): # num을 2~num까지의 수와 나누기
    if num % i == 0: # num이 해당 수로 나눠지면
        print("{}은(는) 소수가 아니다".format(num)) # 소수가 아닐 때
        break # 멈추기
    else:
        print("{}은(는) 소수이다".format(num)) # 소수일 때
        break # 멈추기

# 함수
# n = int(input("수 입력 : "))

# def is_prime(n):
#     if n == 1: return "소수가 아니다" # 1은 소수가 아님
#     elif n == 2: return "소수이다" # 2는 소수이다
#     else:
#         for i in range(2, n+1):
#             if n % i == 0: # 나머지가 0이면 소수가 아니다
#                 s = "{}는 소수가 아니다".format(n)
#                 return s
#             s = "{}는 소수이다".format(n)
#             return s
# print(is_prime(n))