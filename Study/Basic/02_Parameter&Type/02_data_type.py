# 데이터 타입 알아내기
print(type(100))
print(type('Hello'))

# 정수형 사용하기
width = 10
height = 20
print('사각형의 넓이는', width*height, '이다')

radius = 5
PI = 3.14
area = radius * radius * PI
print('원의 넓이는', area, '이다')

# 문자열 데이터 - 출력 및 타입출력
print('abcd')
print(type('abcd'))
print('Hello')
print(type('Hello'))
print('123')
print(type('123'))

# 문자열 데이터 - 문자(ord)와 아스키코드(chr) 반환
print('A')
print('B')
print(ord('A'))
print(ord('B'))
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))

# 여러 줄의 문자열 출력하기
print('개행문자 사용하지 않은 경우')
print('죽는 날까지 하늘을 우러러 한 점 부끄럼 없기를 잎새에 이는 바람에도 나는 괴로워했다')
print('\n')
print('개행문자 사용한 경우')
print('죽는 날까지 하늘을 우러러\n한 점 부끄럼 없기를\n잎새에 이는 바람에도\n나는 괴로워했다')

# 문자열 안에 작은 따옴표 또는 큰 따옴표 표시하기
# 1)큰 따옴표 안에 넣기
strVal = "She's gone"
print(strVal)
# strVal = 'She's gone' //error

# 2)작은 따옴표 안에 넣기
strVal = 'She said "Good Bye"'
print(strVal)

# 3)역 슬래시 사용
strVal1 = 'She\'s gone'
strVal2 = 'She said \'Good Bye\''
print(strVal1)
print(strVal2)

