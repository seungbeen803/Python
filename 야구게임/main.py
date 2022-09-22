import random
origin = [0, 0, 0]
# 데이터 생성
for i in range(0, 3):
    origin[i] = random.randint(0, 9)

    # 중복처리
    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)

    print(origin[i], end=" ")
print()

# 유저 데이터 입력
my_Data = [0, 0, 0]
for i in range(0, 3):
    my_Data[i] = int(input()) # 숫자 옆으로 입력

# 판정
# strike
strike = 0
for i in range(0, 3):
    if(origin[i] == my_Data[i]):
        strike = strike + 1
print(strike, " strike")

# ball
ball = 0
for i in range(0, 3): # origin의 방 번호
    for j in range(0, 3): # my_Data의 방 번호
        if(i != j): # ball 처리 i==j strike에서 처리됨
            if(origin[i] == my_Data[j]):
                ball = ball + 1
print(ball, " ball")





