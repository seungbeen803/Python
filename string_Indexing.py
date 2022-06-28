# 문자열 인덱싱과 슬라이싱
# 인덱싱
s = "Life is too short."
print(s[3])
print(s[11])
print(s[-1])
print(s[-7])
print(s[-18])

# 슬라이싱
s = "Life is too short, You need Python."
print(s[3:7]) # 'e is'
print(s[-10:-7]) # 'ed '
print(s[3:-10]) # 'e is too short, You ne'
print(s[-10:30]) # 'ed Py'
print(s[3:2]) # '' 구할 수 없음
print(s[30:]) # 인덱스 30번부터 맨 뒤까지, 'thon.'
print(s[-7:]) # 'Python'
print(s[:4]) # 맨 앞부터 4번 바로 앞까지, 'Life'
print(s[:-17]) # 'Life is too short,'
print(s[:]) # 맨 앞부터 맨 뒤까지. 즉 문자열 전체, 'Life is too short, You need Python.'

# 문자열 함수
h = "  Happy Programming! app "
print(len(h)) # 글자 수 세기
print(h.count("p")) # 문자열에서 인자 'p'의 개수 세기
print(h.upper()) # 모두 대문자로 변환하기
print(h.lower()) # 모두 소문자로 변환하기
print(h.strip())  # 양쪽 공백 없애기
print(h.replace("Happy", "Funny")) # 문자열 대체하기 (바꾸려는 문자, 바뀐 문자)
print(h.find("app")) # 앞에 app위치가 나옴 왼쪽부터 찾기
print(h.rfind("app")) # 뒤에 app위치가 나옴, 오른쪽부터 찾기
print(h.find("zoo")) # 찾지 못하면 -1리턴

h = "  Happy Programming! "
# 문자열에 인자가 있는지 확인 있으면 true, 없으면 false
print("a" in h) # True 
print("amp" in h) # False
x = "01::23::ab::&&" 
y = x.split("::")
print(y) # ['01', '23', 'ab', '&&']
print(", ".join(y)) # 01, 23, ab, &&

# format : 문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성한다.
# 형식) '{인덱스,0}, {인덱스1}'.format(값0, 값1)
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))
print("name: {name}, number: {num}".format(name = "Jordan", num = 23))

# 정수를 표현하는 여러 가지 방법
print("{:d}".format(515)) # 정수를 넣는다. '515'
print("{:5d}".format(515)) # 최소 5칸을 차지하고 정수를 넣는다. '  515'
print("{:+5d}".format(515)) # 양수면 +를 표시한다. ' +515'
print("{:=+5d}".format(515)) # +를 맨 앞에 표시한다. '+ 515'
print("{:05d}".format(515)) # 빈칸은 0으로 채운다. '00515'
print("{:+05d}".format(515)) # 양수면 0 앞에 +를 표시한다. '+0515'

# 실수를 표현하는 여러 가지 방법
print("{:f}".format(11.17)) # 실수를 넣는다, '11.170000'
print("{:12f}".format(11.17)) # 최소 12칸을 차지하고 실수를 넣는다, '  11.170000'
print("{:12.1f}".format(11.17)) # 최소 12칸을 차지하고 소수점 1자리까지 반올림해서 나타낸다, '        11.2'
print("{:=+6.1f}".format(11.17)) # '+ 11.2'

# 문자열 포매팅
# 문자열을 예쁘게 만드는 방법
# 문자열 중간 특정 부분에 우리가 원하는 값을 넣기 위해 사용하는 것
# 문자열을 만들때 원하는

a = 2
b = 3
s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)
print(s)
# 함수는 앞에 누가 하는지 안나옴
# 메서드는 앞에 누가 하는지 누가 나온다(메서드)

# 직접 대입하기
s1 = 'name : {0}'.format('BlockDMask')
print(s1) # name : BlockDMask

# 변수로 대입하기
age = 55
s2 = 'age : {0}'.format(age)
print(s2) # age : 55

# 이름으로 대입하기
s3 = 'number : {num}, genger : {gen}'.format(num ="1234", gen='남')
print(s3) # number : 1234, genger : 남

# format 문자열의 중괄호의 인덱스
# 인덱스를 입력하지 않으면?
s4 = 'name : {}, city : {}'.format('BlockDMask', 'seoul')
print(s4) # 순서대로 쓸 거면 굳이 인덱스에 값을 주지 않아도 됨(하지만 인덱스 값을 주면 가독성이 높아짐)
# name : BlockDMask, city : seoul

# 인덱스 순서가 바뀌면?
s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
print(s5) # song1 : ice cream, song2 : nunu nana

# 인덱스를 중복해서 입력하면? -> 중복해서 사용 가능
s6 = 'test1 : {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')
print(s6) # test1 : 인덱스0, test2 : 인덱스1, test3 : 인덱스0

# 중괄호 출력 -> 중괄호 2번({{}})적으면 중괄호 출력 가능
s7 = 'Format example. {{}}, {}'. format('test')
print(s7) # Format example. {}, test

# 중괄호로 겹쳐진 인자값 -> 인덱스가 없어도 중괄호가 나옴, 
# 출력할 값을 중괄호로 겹처서 출력하려 하면 이렇게 중괄호 세 개를 쓰면 된다{{{}}}
s8 = 'This is value {{{}}}'.format(1212)
print(s8) # This is value {1212}

# 문자열 정렬하기
# 
# 왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
print(s9) # this is left       | done a     |

# 오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
print(s10) # this is right      | done     b |

# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'a') # 0번 인덱스 : 10자리
print(s11) # this is   center   | done   a   |

# 왼쪽 정렬
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a') # 오른쪽 빈칸은 '-'로 채워라, 'o'로 채워라
print(s12) # this is left------ | done aoooo |

# 오른쪽 정렬
s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b') # 왼쪽 빈칸은 '+'로 채워라, '0'으로 채워라
print(s13) # this is +++++right | done 0000b |

# 가운데 정렬
s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'a') # 양쪽 빈칸을 채움
print(s14) # this is ..center.. | done @@a@@ |

# 정수 N자리 -> 정수를 표현할 때는 문자 사용X
# 정수의 자리수를 표현할 때는 '0Nd'로 표현 N에는 원하는 자릿를 입력
s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(s15) # 정수 3자리 : 12345, 012

# 소수점 N자리
s16 = '아래 2자리: {0:0.2f}, 아래 5자리 : {1:05f}'.format(123.1234567, 3.14) # 2자리 아래가 5이상이면 반올림
print(s16) # 아래 2자리: 123.12, 아래 5자리 : 3.140000

# 구구단 프로그램
a = 2
b = 1
s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)
print(s)