num = int(input("숫자를 입력하세요 : "))
judge = "minus"
judge2 = "odd"

# if num<0:
#     judge = "minus"
# else:
#     judge = "plus"

# if num%2==0:
#     judge2 = "even"
# else:
#     judge2 = "odd"

#중첩 if문
if num>0:
    if num%2==0:
        judge = "plus"
        judge2 = "even"
    else:
        judge = "plus"
        judge2 = "odd"
else:
    if num%2==0:
        judge = "minus"
        judge2 = "even"
    else:
        judge = "minus"
        judge2 = "odd"

print(f"{num}은 {judge}이고 {judge2} 입니다.")