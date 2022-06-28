# 데이터 입력하여 합을 구하는 함수 정의
# 리스트를 하나 선언해서 입력 받은 데이터를 리스트로 변환 시킴
# list = []
# in_list = input("데이터 입력 : ")
# list.append(in_list)

# def func_sum(in_list):
#     sum = 0
#     for i in range(0, len(in_list)):
#         print(list)
#         sum += int(list[i])
#     return sum
# print("합 : ", func_sum(in_list))

list = [] # 빈 리스트 생성
in_list = input("데이터 입력 : ") # input으로 데이터를 입력 받는다
list.append(in_list) # in_list에 저장된 변수를 append를 사용해 list에 넣는다

def func_sum(in_list):
    sum = 0
    list = in_list.split(" ") # 공백을 기준으로 나눈다
    print(list) # 리스트 출력
    for i in range(len(list)): # 0~len(list)까지
        sum += int(list[i])
    return sum
print("합 : ", func_sum(in_list)) # 출력