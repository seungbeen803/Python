# 클래스 메서드 사용한 코드
class Car:
    count = 0

    # 생성자 메서드
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    # 클래스 메서드
    # classmethod와 cls는 짝꿍
    @classmethod
    def get_count(cls):
        return cls.count

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
print(Car.get_count())

# 클래스 메서드를 사용하지 않은 코드
# class Car:
#     count = 0

#     def __init__(self, type, speed):
#         self.type = type
#         self.speed = speed
#         Car.count += 1

#     # @classmethod
#     def get_count(self):
#         return Car.count

# # print(Car.get_count())
# c1 = Car("스포츠카", 100)
# c2 = Car("트럭", 50)
# print(c1.get_count())