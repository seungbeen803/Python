# 1. 셋 생성 : 중복이 없는 자료형
game = {"LOL","Overwatch","Tetris", 1945, 2048}
print(game) # {2048, 'Tetris', 'LOL', 1945, 'Overwatch'}

print(set("Funny")) # {'n', 'y', 'u', 'F'}

# list로 바꿔준다
print([2048, "Tetris", "Cube"]) # [2048, 'Tetris', 'Cube']

# tuple로 바꿔준다
print((2560, 1440)) # (2560, 1440)

# dictionary로 바꿔준다
print({'google': 'google.com', 18: 'unesco.org'}) # {'google': 'google.com', 18: 'unesco.org'}

print(set(range(3))) # {0, 1, 2}

print()

# 2. 셋에 추가
# 하나의 요소 추가
game.add("Fifa")
print(game)

# 여러 요소 추가
game.update(("NBA", "MLB"))
print(game)

print()

# 3. 셋에서 제거
game.remove("LOL")
print(game)

# 4. 셋 연산
# 가. 교집합
s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
s3 & s4
print(s3.intersection(s4)) # {12}

# 나. 합집합
s3 | s4
print(s3.union(s4)) # {3, 4, 6, 8, 9, 12, 16}

# 다. 차집합
s3 - s4
print(s3.difference(s4)) # {9, 3, 6}
