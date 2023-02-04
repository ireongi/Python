# 간단한 함수
def plu(number1, number2):
    return number1 + number2


result1 = plu(10, 20)
print(result1)


# 사칙연산 계산기
def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


num1 = int(input('첫 번째 정수 : '))
num2 = int(input('두 번째 정수 : '))

print(plus(num1, num2))
print(minus(num1, num2))
print(multiple(num1, num2))
print(divide(num1, num2))




