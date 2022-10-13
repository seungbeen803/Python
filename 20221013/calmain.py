import calculator
first_num = int(input("첫 번째 수는? : "))
second_num = int(input("두 번째 수는? : "))

print(first_num, " + ", second_num, " = ", calculator.add(first_num, second_num))
print(first_num, " - ", second_num, " = ", calculator.sub(first_num, second_num))
print(first_num, " * ", second_num, " = ", calculator.mul(first_num, second_num))
print(first_num, " / ", second_num, " = ", calculator.div(first_num, second_num))
