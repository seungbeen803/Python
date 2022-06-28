# 1. 딕셔너리 생성
# 형식 : {키 1 : 값 1, 키 2 : 값 2, 키 3 : 값 3, ...}

d = {}
print(d) # {}

urls = {"google" : "google.com", 18 : "unesco.org"}
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

# 2. 딕셔너리에 요소 추가
urls["x"] = 2560
print(urls) # {'google': 'google.com', 18: 'unesco.org', 'x': 2560}

# 3. 딕셔너리에 요소 수정
urls["x"] = 1920
print(urls) # {'google': 'google.com', 18: 'unesco.org', 'x': 1920}

# 4. 딕셔너리에서 요소 제거
del urls["x"]
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

urls.pop(18)
print(urls) # {'google': 'google.com'}

urls.clear()
print(urls) # {}

# 5. 딕셔너리에서 요소 검색
# 인덱싱 대신 키를 사용하여 자료을 가져옴
# 키 in 딕셔너리, 값 in 딕셔너리.values()

urls = {'google': 'google.com', 18: 'unesco.org'}
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

print(urls["google"]) # 'google.com'

print(urls.get("google")) # 'google.com'

print("google" in urls) # True

print("google.com" in urls) # False

print("google.com" in  urls.values()) # Tr

# 6. 기타 딕셔너리 관련 함수
print(len(urls)) # 2

# 딕셔너리의 키들, 값들을 dict_keys, dict_values 객체로 리턴한다
print((urls.keys())) # dict_keys(['google', 18])
print(urls.values()) # dict_values(['google.com', 'unesco.org'])

# 딕셔너리의 키와 값의 쌍을 묶어 dict_items 객체로 리턴한다
print(urls.items()) # dict_items([('google', 'google.com'), (18, 'unesco.org')])