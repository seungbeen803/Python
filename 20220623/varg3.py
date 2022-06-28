def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + " " + (space * space_num) + args[i]
    print(str)
p(",", 3, "◆", "☆")
p("^", 2, "😋", "😁", "♤")
p("_", 3, "🤣", "😋", "♪", "♡")

# star 함수 정의
def star(shape, *args): # 모양, 개수
    for i in range(len(args)): # 개수의 길이만큼 반복
        print(shape*args[i]) # 출력할 때 모양을 개수만큼 곱해줘서 출력
star("♬", 3)
star("♡", 1, 2, 3)