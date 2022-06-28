# # 1. 2411_최승빈
# tot = 0
# n1 = int(input("점수 입력 1 : "))
# n2 = int(input("점수 입력 2 : "))
# n3 = int(input("점수 입력 3 : "))
# n4 = int(input("점수 입력 4 : "))
# n5 = int(input("점수 입력 5 : "))
# print("입력된 점수 : ", n1, n2, n3, n4, n5)
# tot = n1+n2+n3+n4+n5
# avg = tot / 5.0
# if(avg >= 60):
#     print(avg,"점으로 합격입니다.")
# else:
#     print(avg,"점으로 불합격입니다.")

# # 2
# n1 = int(input("정수 입력 1 : "))
# n2 = int(input("정수 입력 2 : "))

# if n1 > n2:
#     n1, n2 = n2, n1

# for dan in range(n1, n2+1):
#     print('\n{}단'.format(n1))
#     n1 += 1
#     for i in range(1, 10):
#         print("{} x {} = {}".format(dan, i, dan*i))
# print('--------------')

# 3
dict = {"메로나": [1000, 20], "비비빅": [700, 3], "바밤바": [850, 100]}

while(True):
    print('\t')
    print("1. 신규 상품 등록")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 조회")
    print("0. 종료")
    menu = int(input("메뉴 선택 : "))
    print('\n')

    if(menu == 4):
# 3-1
        print("4. 상품 조회\n")
        print("  상품명\t", "가격\t", "수량")

        for key in dict:
            print(key, " \t", dict[key][0], " \t", dict[key][1])
        
    elif(menu == 1):
# 3-2
        print("1. 신규 상품 등록\n")
        newN = input("상품명 입력 : ")
        newP = input("가격 입력 : ")
        newS = input("수량 입력 : ")