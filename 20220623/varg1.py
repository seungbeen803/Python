# 매개 변수에 가변 인수가 있는 함수
def p(*args):
    str = ""
    for a in args:
        str += (a+" ")
    print(str)
p("❤")
p("😋", "😥")
p("💤", "💥", "💤")