# 03. random 모듈을 활용하여 주사위 프로그램을 작성하시오.
import random

def dice_1():
    return int(1 + random.random() * 6)

def dice_2():
    return random.choice([1, 2, 3, 4, 5, 6])

def dice_3():
    return random.randrange(1, 7)

print(dice_1())
print(dice_2())
print(dice_3())