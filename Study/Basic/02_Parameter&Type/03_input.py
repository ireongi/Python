# 키보드로 값 입력받기

# input() 사용
strVal = input('좋아하는 것은 무엇인가요?\n: ')
print(strVal + '을/를 좋아합니다')

strID = input('아이디를 입력하세요: ')
strPW = input('비밀번호를 입력하세요: ')
print('입력한 ID는 ' + strID + '입니다')
print('입력한 PW는 ' + strPW + '입니다')

# Input Data Operations
# Wrong Output
Num1 = input('첫 번째 숫자를 입력하세요: ')
Num2 = input('두 번째 숫자를 입력하세요: ')
print('두 수의 합은 ' + Num1 + Num2 + '입니다')

total = Num1 + Num2
print('두 수의 합은 ' + total + '입니다')
