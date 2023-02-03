# 관계 연산자
first = 10
second = 11
third = 12
four = 13

print(first == second)
print(first < second)
print(first >= third)
print(first != four)

# 논리 연산자
print(not(first == second))
print((first > second) and (first < four))
print((first > second) or (first < four))

# 3항 연산자
val = True
print(val and 1 or 0)
val = False
print(val and 1 or 0)

# 활용
money = int(input('돈을 넣어주세요 : '))
count = int(input('몇 개 드릴까요? : '))
icecream = 1200

money -= count * icecream
change = '거스름돈 : ' + str(money)
results = money < 0 and '잔액이 부족합니다. 금액을 투입해주세요.\n' or change
print(results)