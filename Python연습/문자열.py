# 1. 문자열 다루기
greeting = 'Hello'
to = 'world!'
print(greeting) # Hello
print(type(greeting)) # <class 'str'>

say_hello = greeting + ", " + to
print(say_hello) # Hello, world!

print("Hello"*5) # HelloHelloHelloHelloHello

print("\"Hello\"\n" + to)
# "Hello" <- 출력할 때 따옴표가 나오게 하려면 \"을 사용하면 된다!
# world!

multiline = """Happy
Programming"""
print(multiline)
# Happy
# Programming

# 2. 문자열 인덱싱과 슬라이싱

# 인덱싱
# 형식 : 문자열[인덱스]
s = "Life is too short."
print(s) # Life is too short.

print(s[3]) # e
print(s[11]) # ' '
print(s[-1]) # .
print(s[-7]) # ' '
print(s[-18]) # L

# 슬라이싱
# 형식 : 문자열[인덱스 1 : 인덱스 2]
# 마지막 숫자보다 -1해서 나옴
s = "Life is too short, You need Python."
print(s) # Life is too short, You need Python.

print(s[3:7]) # 'e is'
print(s[-10:-7]) # 'ed '
print(s[3:-10]) # 'e is too short, You ne'
print(s[-10:30]) # 'ed Py'
print(s[3:2]) # '' 구할 수 없음
print(s[30:]) # 'thon.'
print(s[-7:]) # 'Python.'
print(s[:4]) # 'Life'
print(s[:-17]) # 'Life is too short,'
print(s[:]) # Life is too short, You need Python.

# 3. 문자열 함수
h = "  Happy Programming! "
print(h) # '  Happy Programming!'
# len : 글자 수 세기
print(len(h)) # 21

print(h.count("p")) # 2
print(h.upper()) # '  HAPPY PROGRAMMING!'
print(h.lower()) # '  happy programming!'
print(h.strip()) # 'Happy Programming!'
print(h.replace("Happy", "Funny")) # '  Funny Programming!'
# 왼쪽부터 인자 값 찾기
print(h.find("ap")) # 3
# 오른쪽부터 인자 값 찾기
print(h.rfind("a")) # 3
print(h.find("zoo")) # -1 : 찾지 못하면 -1을 리턴한다.

h = "  Happy Programming! "
# 문자열 안에 있는지 확인하기
print("a" in h) # True
print("amp" in h) # False

x = "01::23::ab::&&"
# 문자열을 나누어 리스트 만들기 괄호안에는 기준을 넣는다
y = x.split("::") 
print(y) # ['01', '23', 'ab', '&&'] 

# 리스트를 문자열로 변환할 때 join을 사용
print(", ".join(y)) # 01, 23, ab, &&

# format : 문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성한다.
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True)) # name: Ronaldo, number: 7, soccer: True
print("name: {name}, number: {num}".format(name = "Jordan", num = 30)) # name: Jordan, number: 30

# 정수를 표현하는 여러 가지 방법
print("{:d}".format(515)) # '515'
print("{:5d}".format(515)) # 최소 5칸을 차지하고 정수를 넣음 -> '     515'
print("{:+5d}".format(515)) # 양수면 +를 표시 -> ' +515'
print("{:=+5d}".format(515)) # +를 맨 앞에 표시 -> "+ 515"
print("{:05d}".format(515)) # 빈칸은 0으로 채움 -> '00515'
print("{:+05d}".format(515)) # 양수면 0앞에 +를 표시 -> '+0515'

# 실수를 표현하는 여러가지 방법
print("{:f}".format(11.17)) # '11.170000'
print("{:12f}".format(11.17)) # '   11.170000'
print("{:12.1f}".format(11.17)) # '        11.2'

# 위의 문자열 format을 사용하여 양수 11.17을 '+ 11.2'로 출력해보자.
print("{:=+6.1f}".format(11.17)) # '+ 11.2'