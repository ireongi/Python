# 관계 연산자
a = 10
b = 11
c = 12
d = 13

print(a == b)
print(a < b)
print(a >= c)
print(a != d)

# 논리 연산자
print(not(a == b))
print((a > b) and (a < d))
print((a > b) or (a < d))

# 3항 연산자
value = True
print(value and 1 or 0)
value = False
print(value and 1 or 0)

# 활용
money = int(input('돈을 넣어주세요 : '))
count = int(input('몇 장 드릴까요? : '))
ticket = 1200

money -= count*ticket
change = '거스름돈 : ' + str(money)
results = money < 0 and '잔액이 부족합니다. 금액을 투입해주세요.\n' or change
print(results)