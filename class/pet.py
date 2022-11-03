# Pet 클래스 정의
# 클래스 안에 첫 번째 메서드는 self
class Pet:
    # 짖다
    def bark_dog(self): # p1
        print("멍멍~")
    def bark_cat(self): # p2
        print("야옹~야옹~")
    def bark_hamster(self): # p3
        print("찍찍~")

# 클래스 사용
p1 = Pet()
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_hamster()