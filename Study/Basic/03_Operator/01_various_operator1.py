# 산술 연산자
num1 = 5
num2 = 3

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 ** num2) #num2를 지수로 갖게됨
print(num1 / num2) #두 수의 나누기(몫 구하기 x)
print(num1 // num2) #두 수를 나눈 몫의 소수점을 버린 수
print(num1 % num2)

# 대입 연산자
num1 += num2
print(num1)
num1 -= num2
print(num1)
num1 *= num2
print(num1)
num1 **= num2
print(num1)
num1 /= num2
print(num1)
num1 //= num2
print(num1)
num1 %= num2
print(num1)

# 활용
money = int(input('돈을 넣어주세요 : '))
count = int(input('몇 장 드릴까요? : '))
ticket = 1200

money -= count*ticket
print('거스름돈 :', money)




