# Type Casting - Convert to Integer
print(int('10'))
print(int(3.123))
print(int('10')+int(3.123))

# Type Casting - Convert to String
print(str(10))
print(str(3.14))
print(str(10)+str(3.14))

# Correct Output
strNum1 = input('첫 번째 숫자를 입력하세요: ')
strNum2 = input('두 번째 숫자를 입력하세요: ')
total = int(strNum1) + int(strNum2)
print('두 수의 합은 ' + str(total) + '입니다') # 문자열과 결합하여 출력하기 위해서 문자열로 캐스팅해야함
print('두 수의 합은', total, '입니다')

# Various Casting
print(float(10))
print(ord('A'))
print(chr(65))