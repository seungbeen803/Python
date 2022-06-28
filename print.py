print('Python start!')
print("Python start!")
print("""Python start!""")
print('''Python start!''')

print()

# separator 사용
print('P', 'Y', 'T', 'H', 'O', 'N', sep="")
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

# end 사용
print('Welcom To', end=' ') # 한 줄에 다찍기 위해 공백을 줌
print('IT News', end=' ')
print('Web Site')

print()
import sys

print('learn Python', file=sys.stdout) # 기본 출력 장치로 출력한다는 의미