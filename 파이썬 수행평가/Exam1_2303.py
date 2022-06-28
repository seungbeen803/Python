# #2303 박선주
# #1.
start = int(input("정수1 입력 : "))
end = int(input("정수2 입력 : "))

if start < end:
    for i in range(start, end+1):
        print(f"\n{i}단")
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")
else:
    for i in range(end, start+1):
        print(f"\n{i}단")
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")

            
# #2.
print()
score = [0, 0, 0, 0, 0]
sum = 0
avg = 0
count = 0
for i in range(0,5):
    score[i] = int(input(f"점수 {i} 입력 : "))
    sum += score[i]
    count += 1

avg = sum / count
print(f"입력된 점수 : {score[0]}  {score[1]}  {score[2]}  {score[3]}  {score[4]}")
print(f"합계 : {sum}")
print("평균 : %.2f" % avg)
if avg >=60:
    print("%.2f점으로 합격입니다." % avg)
else:
    print("%.2f점으로 불합격입니다." % avg)

#3.
ice = {"메로나" : [1000,20], "비비빅" : [700,3], "바밤바" : [850,100]}
#3-1
print()
print("4. 상품 조회")
print("  상품명    가격     수량")
for key in ice:
    print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")
    # print(key,"    ",ice[key][0],"    ", ice[key][1])   

#3-2
print()
print("1. 신규 상품 등록")
new_key = input("상품명 입력 : ")
new_key_value = [0, 0]
new_key_value[0] = int(input("가격 입력 : "))
new_key_value[1] = int(input("수량 입력 : "))
ice[new_key] = new_key_value
print("  상품명    가격     수량")
for key in ice:
    print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")

#3-3
print()
print("2. 상품 수정")
fix_key = input("상품명 입력 : ")
print("1. 가격 수정")
print("2. 수량 수정")
menu = input("메뉴 입력 : ")
if menu == "1":
    price = input("가격 입력 : ")
    ice[fix_key][0] = price
else:
    count = input("수량 입력 : ")
    ice[fix_key][1] = count
print("  상품명    가격     수량")
for key in ice:
    print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")

#3-4
print()
print("3. 상품 삭제")
del_key = input("상품명 입력 : ")
del ice[del_key]
print("  상품명    가격     수량")
for key in ice:
    print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")

#3-5
print()
print("1. 신규 상품 등록")
print("2. 상품 수정")
print("3. 상품 삭제")
print("4. 상품 조회")
print("0. 종료")
while True:
    menu = input("메뉴 입력 : ")
    if menu == "0":
        break


#3-6
while True:
    print()
    print("1. 신규 상품 등록")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 조회")
    print("0. 종료")
    menu = int(input("메뉴 입력 : "))
    if menu == 1:
        print()
        print("1. 신규 상품 등록")
        new_key = input("상품명 입력 : ")
        new_key_value = [0, 0]
        new_key_value[0] = int(input("가격 입력 : "))
        new_key_value[1] = int(input("수량 입력 : "))
        ice[new_key] = new_key_value
        print("  상품명    가격     수량")
        for key in ice:
            print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")
    elif menu == 2:
        print()
        print("2. 상품 수정")
        fix_key = input("상품명 입력 : ")
        print("1. 가격 수정")
        print("2. 수량 수정")
        menu = input("메뉴 입력 : ")
        if menu == "1":
            price = input("가격 입력 :")
            ice[fix_key][0] = price
        else:
            count = input("수량 입력 : ")
            ice[fix_key][1] = count
        print("  상품명    가격     수량")
        for key in ice:
            print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")
    elif menu == 3:
        print()
        print("3. 상품 삭제")
        del_key = input("상품명 입력 : ")
        del ice[del_key]
        print("  상품명    가격     수량")
        for key in ice:
            print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")
    elif menu == 4:
        print()
        print("4. 상품 조회")
        print("  상품명    가격     수량")
        for key in ice:
            print(f"{key}      {ice[key][0]:>5}     {ice[key][1]:>3}")
    elif menu == 0:
        print("프로그램을 종료합니다.")
        break
    
        
