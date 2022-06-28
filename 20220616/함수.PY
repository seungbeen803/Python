# 함수 정의
def times(a, b):
    return a*b
print(times)
print(times(10, 5))

myTimes = times
print(times)
print(times(10, 5))

print(myTimes)
print(myTimes(10, 5))

# 수학 관련 내장 함수
# 가. 절댓값 : abs(x)
print(10, "의 절댓값 : ", abs(10))
print(-10, "의 절댓값 : ", abs(10))

# 나. 진수 변환: bin(n), oct(n), hex(n)
# 10진수 -> 2진수 변환
print(128, "의 2진수 : ", bin(128))
print(255, "의 2진수 : ", bin(255))

# 10진수 -> 8진수 변환
print(7, "의 8진수 : ", oct(7))
print(8, "의 8진수 : ", oct(8))

# 10진수 -> 16진수 변환
print(15, "의 16진수 : ", hex(15))
print(16, "의 16진수 : ", hex(16))

# 다. 연산 : max(), min(), sum(), pow()
# 연산
numbers = [ 1, 5, -2, 0, 6 ]
print(numbers, "중 가장 큰 값은 ", max(numbers))
print(numbers, "중 가장 작은 값은 ", min(numbers))
print(numbers, "합계는 ", sum(numbers))
print("2의 10승은", pow(2, 10))

# 라. 반올림 : round()
# 반올림
pi = 3.14152
print(pi,"의 소수점 1자리 반올림은", round(pi))
print(pi,"의 소수점 1자리 반올림은", round(pi, 0))
print(pi,"의 소수점 2자리 반올림은", round(pi, 1))
print(pi,"의 소수점 3자리 반올림은", round(pi, 2))
print(pi,"의 소수점 4자리 반올림은", round(pi, 3))

# 3. 문자열 관련 내장 함수와 문자열 형 변환 함수
user_name = input("이름은? ")
user_age = input("나이는? ")
print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
print(say.format(user_name, user_age))

pi = "3.14159"
print("문자열 출력 :", pi)
print("실수 변환 출력:", float(pi))
print(float(pi)+100)
year = "2018"
print("올해 연도:", year)
print("100년 뒤는", int(year) + 100, "년입니다.")
print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 " + str(year) + "년입니다.")

# 4. 리스트 관련 내장 함수
list = ['d', 'c', 'a', 'b']
list.reverse()
# print("리스트 항목 순서 뒤집기", list)
# list.sort()
print("리스트 항목 정렬하기", list)
list.sort(reverse=True)
print("리스트 항목 역정렬하기", list)
for index, value in enumerate(list):
    print("인덱스", index, "위치의 값은 ", value)

# 5. 내장 함수와 똑같은 이름의 변수 사용
str = "문자열"
print(str)
n = 3
print(str(n))

