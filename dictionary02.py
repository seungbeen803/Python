# 1. 딕셔너리 생성
d = {}
print(d) # {}

urls = {"google":"google.com", 18:"unesco.org"}
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

print()

# 2. 딕셔너리에 요소 추가
urls["x"] = 2560
print(urls) # {'google': 'google.com', 18: 'unesco.org', 'x': 2560}

print()

# 3. 딕셔너리에 요소 수정
urls["x"] = 1920
print(urls) # {'google': 'google.com', 18: 'unesco.org', 'x': 1920}

print()

# 4. 딕셔너리에서 요소 제거
del urls["x"]
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

urls.pop(18)
print(urls) # {'google': 'google.com'}

urls.clear()
print(urls) # {}

print()

# 5. 딕셔너리에서 요소 검색
urls = {'google': 'google.com', 18: 'unesco.org'}
print(urls) # {'google': 'google.com', 18: 'unesco.org'}

print(urls["google"]) # google.com
 
print(urls.get("google")) # google.com

print("google" in urls) # True

print("google.com" in urls) # False

print("google.com" in urls.values()) # True