import calculator as cal

first_num = int(input("첫 번째 수는? : "))
second_num = int(input("두 번째 수는? : "))

print(first_num, " + ", second_num, " = ", cal.add(first_num, second_num))
print(first_num, " - ", second_num, " = ", cal.sub(first_num, second_num))
print(first_num, " * ", second_num, " = ", cal.mul(first_num, second_num))
print(first_num, " / ", second_num, " = ", cal.div(first_num, second_num))
