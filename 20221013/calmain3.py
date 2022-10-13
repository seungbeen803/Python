from calculator import *

first_num = int(input("첫 번째 수는? : "))
second_num = int(input("두 번째 수는? : "))

print(first_num, " + ", second_num, " = ", add(first_num, second_num))
print(first_num, " - ", second_num, " = ", sub(first_num, second_num))
print(first_num, " * ", second_num, " = ", mul(first_num, second_num))
print(first_num, " / ", second_num, " = ", div(first_num, second_num))