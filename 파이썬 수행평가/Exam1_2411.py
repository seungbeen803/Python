# 1. 2411_최승빈
sum = 0
n1 = int(input("점수1 입력 : "))
n2 = int(input("점수2 입력 : "))
n3 = int(input("점수3 입력 : "))
n4 = int(input("점수4 입력 : "))
n5 = int(input("점수5 입력 : "))
print("입력된 점수 :",n1,n2,n3,n4,n5)
sum = n1+n2+n3+n4+n5
print("합계: ",sum)
avg = sum / 5.0
print("평균: ",avg)
if(avg >= 60):
    print(avg,"점으로 합격입니다.")
else:
    print(avg,"점으로 불합격입니다.")

# 2
dan = int(input("정수 입력 1 : "))
dan1 = int(input("정수 입력 2 : "))

if dan > dan1:
    dan, dan1 = dan1, dan

for dans in range(dan, dan1+1):
        print('\n{}단'.format(dan))
        dan += 1
        for i in range(1, 10):
            print("{} x {} = {}".format(dans, i, dan*i))
print('--------------')

# 3
dict = {"메로나": [1000, 20], "비비빅":[700, 3], "바밤바": [850, 100]}

while(True):
    print("\t")
    print("1. 신규 상품 등록")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 조회")
    print("0. 종료")
    menu = int(input("메뉴 선택 : "))
    print("\n")

    if(menu == 4):
    # 3-1
        print("4 . 상품 조회\n")
        print("  상품명\t", "가격\t", "수량")

        for key in dict:
            print(key, " \t", dict[key][0]," \t", dict[key][1])

    elif(menu == 1):
    # 3-2
        print("1. 신규 상품 등록")
        newN = input("상품명 입력 : ")
        newP = input("가격 입력 : ")
        newS = input("수량 입력 : ")
        dict[newN] = [newP, newS]
        print("\t상품명\t가격\t수량")
        for key in dict:
            print(key, " \t", dict[key][0]," \t", dict[key][1])

    elif(menu == 2):
    # 3-3
        print("2. 상품 수정")
        name = input("상품명 입력 : ")
        print("1. 가격 수정")
        print("2. 수량 수정")
        menu = int(input("메뉴 입력 : "))
        if(menu == 1):
            sP = input("가격 입력 : ")
            dict[name][0] = sP
        else:
            sN = input("수량 입력 : ")
            dict[name][1] = sN
        print("\t상품명\t가격\t수량")
        for key in dict:
            print(key, " \t", dict[key][0]," \t", dict[key][1])
    
    elif(menu == 3):
    # 3-4
        print("3. 상품 삭제")
        name = input("상품명 입력 : ")
        dict.pop(name)
        print("\t상품명\t가격\t수량")
        for key in dict:
            print(key, " \t", dict[key][0]," \t", dict[key][1])

    elif(menu == 0):
    # 3-5
        print("프로그램을 종료합니다.")
    break

