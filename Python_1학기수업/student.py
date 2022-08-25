# 1. 내 정보
student_grade =  2
print(student_grade)

student_class = 4
print(student_class)

student_number = 11
print(student_number)

student_name = "최승빈"
print(student_name)

student_height = 163.0
print(student_height)

print()

# 2. 각 변수의 자료형
print(type(student_grade))
print(type(student_class))
print(type(student_number))
print(type(student_name))
print(type(student_height))

print()

# 3. 2-4반 출력
our_team = ['김민영', '김예진', '신유림', '양서영', '오나현', '유정은', '윤성현', '임수민', '최가을', '최승빈', '최원서', '황채민']
print(our_team)

print()

# 4. 10번 학생의 이름 출력
print(our_team[9])

# 5. 6번부터 9번 학생의 이름을 출력
print(our_team[5:9])

# 6. 반 학생의 이름을 키로하고, 값에는 그 학생의 동아리 이름은 딕셔너리 변수 club에 담아보자.
club = {"김민영":"앱앤미", "김예진":"LSC", "신유림":"JS", "양서영":"없음", "오나현":"LSC", "유정은":"PP", "윤성현":"없음", "임수민":"MAS", "최가을":"CPU", "최승빈":"앱앤미", "최원서":"LSC", "황채민":"CPU"}
print(club)

# 7. 5번 학생의 이름으로 동아리 이름을 출력해보자
print(club["오나현"])

# 8. 1번 학생의 이름을 모를 때, 번호로 동아리 이름을 구해 보자. (our_team을 이용하여 club에서 가져온다)
print(club[our_team[0]])
