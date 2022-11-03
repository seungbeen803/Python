class Person:
    # 생성자
    # 생성자 : __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('-'*30)
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        print('-'*30)


# 클래스 사용
p1 = Person('홍길동', 20)
p1.print_info()

p2 = Person('강감찬', 40)
p2.print_info()

p3 = Person('을지문덕', 30)
p3.print_info()
