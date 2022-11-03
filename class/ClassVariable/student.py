# 클래스의 인스턴스 객체가 생성될 때마다 카운트를 1씩 증가시키는 클래스 구현
# 이 때 카운트 증가 함수는 클래스 내 메서드를 통해서 구현
class Student:
    # 클래스 변수
    count_class_var = 0

    # 생성자
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        Student.increase_obj(self)

    def increase_obj(self):
        Student.count_class_var += 1

# 클래스 사용
print('현재까지 생성된 인스턴스 객체의 개수 :', Student.count_class_var)
s1 = Student('유', 17, 10)
print('현재까지 생성된 인스턴스 객체의 개수 :', Student.count_class_var)
s2 = Student('이', 18, 20)
print('현재까지 생성된 인스턴스 객체의 개수 :', Student.count_class_var)
s3 = Student('임', 19, 8)
