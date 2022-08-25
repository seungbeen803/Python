money = 1
if money:
    # money가 0이면 "타고 가자"만 나온다
    print("택시를")
print("타고")
    # print("가자") // Error 발생

money = 1
if money:
    print("택시를")
print("타고")
print("가자")

money = 2000
if money>3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라") # 걸어 가라

money = 2000
card = 1
if money>3000 or card: 
    print("택시를 타고 가라")
else:
    print("걸어 가라") # 택시를 타고 가라

print()

pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라") # 택시를 타고 가라

print()

pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket: # 조건문을 바꿀 필요없음
    pass # 넘어갈 수 있다
else:
    print("카드를 꺼내라") # 택시를 타고 가라
print("수행완료") # 수행완료

print()

if "money" in pocket:
    print("카드를 꺼내라")
print("수행완료")

print()

# 만약 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라.
# 중첩 if
pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라 - money")
elif 'card' in pocket:
    print("택시를 타고 가라 - card")
else:
    ("걸어 가라")

# 실행 결과 출력되는 것은
saying = "Life is too short, you need python"

if "wife" in saying : print("wife")
elif "python" in saying and "you" not in saying : print("python")
elif "shirt" not in saying : print("shirt")
elif "need" in saying : print("need")
else : print(none) # shirt

