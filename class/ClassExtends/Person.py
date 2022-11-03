class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + "가 " + food + "를 먹습니다.")

    def __str__(self):
        return self.name + "는 " + str(self.age) + "살 입니다."

