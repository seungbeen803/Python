import area2

area2.print_area(10, 20)
area2.print_area(20, 30)

for i in range(11, 15):
    area2.print_area(i, 20)

print("가로 30 세로 10인 사각형의 넓이는 ", area2.box_area(30, 10))
# area2를 불러왔기 때문에 area2이다
print(area2.__name__)
# print(__name__) # main