# for문으로 구구단 출력하기

# 2단 출력
for i in range(1, 10, 1):
    print("2 * %d = %d" %(i, 2*i))

# 전체 출력
for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("%d * %d = %d" %(i, k, i*k), end=' / ')
print(' ')

# 입력받은 단만 출력
dan = int(input('원하는 단을 입력하시오 : '))
for i in range(1, 10, 1):
    print("%d * %d = %d" %(dan, i, i*dan))

# 별 찍기 v1
star = '*'
for i in range(1, 6, 1):
    print(i*star)

# 별 찍기 v2
star = '*'
for col in range(1, 6, 1):
    for row in range(0, col, 1):
        print(star, end = " ")
    print('')        