#소수판정 프로그램

number = int(input('input integer number : '))
counts = 0  # primenumber 판정용도

for k in range(1, number+1): #1부터 입력된 수까지 반복
    if number % k == 0:
        counts = counts + 1

if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')