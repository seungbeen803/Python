# 1. 셋 생성
# 형식 : {값 1, 값 2, 값 3}

game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game) # {2048, 'Overwatch', 'Tetris', 1942, 'LOL'}

# set(문자열) : 문자열의 문자가 하나씩 셋의 요소로 들어간다.
print(set("Funny")) # {'y', 'F', 'u', 'n'}

# set(리스트) : 리스트의 각 요소가 하나씩 셋의 요소로 들어간다.
print(set([2048, "Tetris", "Cube"])) # {2048, 'Cube', 'Tetris'}

# set(튜플) : 튜플의 각 요소가 하나씩 셋의 요소로 들어간다.
print(set((2560, 1440))) # {2560, 1440}

# set(딕셔너리) : 딕셔너리의 키가 하나씩 셋의 요소로 들어간다.
print(set({"google":"google.com", 18:"unesco.org"})) # {18, 'google'}

# set(range()) : range()함수의 각 요소가 하나씩 리스트의 요소로 들어간다.
print(set(range(3))) # {0, 1, 2}

# 2. 셋에 추가
# add() : 요소 하나를 추가할 때 사용
# update() : 여러 요소를 추가할 때 사용
game.add("Fifa")
print(game) # {2048, 'Tetris', 'Overwatch', 1942, 'Fifa', 'LOL'}
game.update(("NBA", "MLB")) # {'Tetris', 2048, 'Overwatch', 'Fifa', 'NBA', 'MLB', 1942, 'LOL'}
print(game)

# 3. 셋에서 제거
game.remove("LOL")
print(game) # {2048, 'Tetris', 1942, 'NBA', 'Fifa', 'MLB', 'Overwatch'}

game.remove("Overwatch") # {2048, 'Tetris', 1942, 'Fifa', 'NBA', 'MLB'}
print(game)

# 4. 셋 연산

# 가. 교집합
s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
print(s3 & s4) # {12}
print(s3.intersection(s4)) # {12}

# 나. 합집합
print(s3 | s4) # {3, 4, 6, 8, 9, 12, 16}
print(s3.union(s4)) # {3, 4, 6, 8, 9, 12, 16}

# 다. 차집합
print(s3 - s4) # {9, 3, 6}
print(s3.difference(s4)) # {9, 3, 6}

# 라. 대칭 차집합
print(s3 ^ s4) # {3, 4, 6, 8, 9, 16}
print(s3.symmetric_difference(s4)) # {3, 4, 6, 8, 9, 16}
