# 구구단 프로그램
a = 2
b = 1
# s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)

# 파이썬은 들여쓰기가 중요한 언어이다. (중괄호가 없다) 들여쓰기 중요 잘하기!!!
# 어떤 범위 안에서 돌아가게할 때  range를 사용한다.
for a in range(2, 10):  # 3단까지 인데 항상 뒤에는 -1 -> 4 - 1 = 3
    print('{0}단'.format(a))
    for b in range(1, 10): # 조건문이나 반복문 뒤에는 :을 써준다!!!
        print('{0} x {1} = {2:2}'.format(a, b, a*b)) # 2:2 2자리 지정

# % 서식문자
num = 50
s = 'my age %d' % num
print(s)

# % r기호 문자 출력
names = ['kim', 'park', 'lee']
for name in names: # for 변수 in 범위
    print('my name is %s' % name)

# % 기호 정수 출력
money = 10000
s2 = 'give me %d won' % money
print(s2)

# % 기호 실수 출력
d = 3.141592
print('value %f' % d)

# 포매팅 해야할 변수 값이 두 개 이상일 때
# 출력해야할 값이 두 개 이상인 경우()를 이용합니다
s1 = 'my name is %s, age : %d' % ('mirim', 100)
print(s1)

# 출력해야할 값이 점점 많아질수록
age = 78
money = 20000
name = 'Jang'
weight = 63.12
etc = 'abcde'
s2 = 'my name is %s, age : %d, weight : %f, money : %d, etc : %s' % (name, age, weight, money, etc)

# string formattion - 문자열 포매팅
month = 1
while month <= 12:
    print(f'2020년 {month}월')
    month = month + 1

# 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다.
s = 'coffee'
n = 5
result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result)

# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)

# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
# f-string 오른쪽 정렬
s3 = 'right'

result3 = f'|{s3:>10}|'
print(result3)

# f-string 중괄호 출력
num = 10
result = f'my age {{{num}}}, {{num}}' # 중괄호 3개 쓰면 {{{num}}} : 변수로 표현, {{ num}} : 그냥 num글씨 출력(문자열)
print(result)

# f-string과 딕셔너리
# 딕셔너리 -> 키 : 값 
d = {'name' :'Mirim', 'gender' : 'female', 'age' : 18}
result = f'my name {d["name"]}, gender {d["gender"]}, age{d["age"]}'
print(result)

# f-string과 리스트
# 문장이 단순해짐
n = [100, 200, 300]
print(f'list : {n[0]}, {n[1]}, {n[2]}')

for v in n:
    print(f'list with for : {v}')


strB = "파이썬 연습"
print(len(strB)) # 6