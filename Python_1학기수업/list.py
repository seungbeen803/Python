# 리스트
colors = ["red", "green", "blue"]
print(colors) # ['red', 'green', 'blue']
print(type(colors)) # <class 'list'>

# append() 메서드 : 기존 리스트에 값 하나를 추가
print(colors) # ['red', 'green', 'blue']
colors.append("blue")
print(colors) # 맨 뒤에 값을 추가한다. ['red', 'green', 'blue', 'blue']

# insert() 메서드 : 원하는 위치에 값을 추가
print(colors) # ['red', 'green', 'blue', 'blue']
colors.insert(1, "black")
print(colors) # ['red', 'black', 'green', 'blue', 'blue']

print(colors) # ['red', 'black', 'green', 'blue', 'blue']
print(colors.index("red")) # 0
colors+=["red"] #  red를 맨 뒤에 추가
print(colors) # ['red', 'black', 'green', 'blue', 'blue', 'red']
print(colors.index("red", 1)) # 1번방 이후에 있는 red를 찾는다, 5
colors+= "red" #  마지막에 red가 추가되면서 'r', 'e', 'd'가 추가 됨
print(colors) # ['red', 'black', 'green', 'blue', 'blue', 'red', 'r', 'e', 'd']

print()

# count() 메서드 : 현재 해당 값의 개수를 반환
print(colors) # ['red', 'black', 'green', 'blue', 'blue']
print(colors.count("red")) # red의 개수 2
print()

# pop() 메서드 : 값을 뽑아내서 반환
print(colors.pop()) # d
print(colors.pop()) # e
print(colors.pop(1)) # black 1번 위치의 값을 뽑아낸다
print(colors)  # ['red', 'green', 'blue', 'blue', 'red', 'r']
print()

# remove() 메서드 : 단순히 해당 값을 삭제
print(colors) # ['red', 'green', 'blue', 'blue', 'red', 'r']
#print(colors.remove("blue")) # None remove는 print를 쓰지 않아도 된다
colors.remove("blue")
print(colors) # ['red', 'green', 'blue', 'red', 'r']
print()

# extend() 메서드 : 데이터 추가
print(colors) # ['red', 'green', 'blue', 'red', 'r']
colors.extend(["blue", "yellow", "white"])
print(colors) # ['red', 'green', 'blue', 'red', 'r', 'blue', 'yellow', 'white']

# sort() 메서드 : 오름차순 정렬
print(colors)
colors.sort()
print(colors) # ['blue', 'blue', 'green', 'r', 'red', 'red', 'white', 'yellow']

# reverse() 메서드 : 내림차수 정렬
colors.reverse()
print(colors) # ['yellow', 'white', 'red', 'red', 'r', 'green', 'blue', 'blue']

