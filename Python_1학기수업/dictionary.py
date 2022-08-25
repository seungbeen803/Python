# key를 통해 값을 찾음
d = dict(a=1, b=2, c=3)
print(d) #{'a': 1, 'b': 2, 'c': 3}
print(type(d)) # <class 'dict'>

# apple이 key가 되고 red가 값이 된다.
colors = {"apple" : "red", "banana" : "yellow"}
print(colors) # {'apple': 'red', 'banana': 'yellow'}

colors["cherry"] = "red"
print(colors) # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

for item in colors.items():
    print(item)
# ('apple', 'red')
# ('banana', 'yellow')
# ('cherry', 'red')

for k, v in colors.items():
    print(k, v)
# apple red
#banana yellow
# cherry red

print()

# 부분 삭제
print(colors)
del colors["cherry"]
print(colors)

# 전체 삭제
colors.clear()
print(colors) # {}


device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
device["아이맥"] = 15 # 없는 내용은 추가가 된다
device["아이폰"] = 6 # 동일한 key가 있다면 그 key의 값을 변경해줌
print(device) # {'아이폰': 6, '아이패드': 10, '윈도우타블렛': 20, '아이맥': 15}
del device["아이폰"]
print(device) # {'아이패드': 10, '윈도우타블렛': 20, '아이맥': 15}

# 메서드 - keys(), values()
phone = {"kim" : "1111", "lee" : "2222", "park" : "3333"}
print(phone.keys()) # key값 들만, dict_keys(['kim', 'lee', 'pork'])
print(phone.values()) # 값 들만, dict_values(['1111', '2222', '3333'])

print("park" in phone) # True
print("moon" in phone) # False

p = phone
print(p) # {'kim': '1111', 'lee': '2222', 'park': '3333'}

#for문으로 참조하기
d = {"a" : 100, "b" : 200, "c" : 300}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)
