# while

# 반복
iloop = 0
while iloop < 5:
    print("@")
    iloop += 1

# 1부터 10까지의 합 구하기
sum = 0
val = 0
while val < 11:
    sum += val # 0부터 10까지 1씩 증가하며 합산됨
    val += 1 # 0부터 10까지 1씩 증가
print('1~10 sum: '+str(sum))

# 1부터 100까지 홀수의 합 구하기
sum = 0
val = 1
while val < 101:
    sum += val
    val += 2
print('1~10 홀수 sum :', sum)
