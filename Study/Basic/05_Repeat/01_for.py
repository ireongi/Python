# for~

for num in range(0, 5, 1): # 0부터 4까지 1씩 증가
    print("@")

for num in range(0, 5, 1):
    print(num + 1, ": @")


sum = 1+2+3+4+5+6+7+8+9+10
print('1~10 sum:',sum)

sum1 = 0
for i in range(1, 11, 1): # 1부터 10까지 1씩 증가
    sum1 += i # sum1에 range만큼 i 더함
print('1~10 sum:', sum)

sum2 = 0
for i in range(1, 1001, 1):
    sum2 += i
print('1~1000 sum:', sum2)

for i in range(1, 10, 1):
    print(str(i)+'day') # ,로 인한 띄어쓰기 방지


sum3 = 0
for i in range(0, 101, 2): # 0부터 2씩 증가하므로 짝수의 합을 구할 수 있음
    sum3 += i
print('1~100 중 2의 배수 :', sum3)


a = int(input('숫자 : '))
s = int(input('범위 시작값 : '))
e = int(input('범위 끝값 : '))

for i in range(s, e, 1):
    if(a == i):
        print('그 숫자가 있습니다.')
print('그 숫자가 없습니다.')