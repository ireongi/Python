#prime number v0.1

# number = int(input('input integer number : '))
# counts = 0  # primenumber 판정용도
#
# for k in range(1, number+1): #1부터 입력된 수까지 반복
#     if number % k == 0:
#         counts = counts + 1
#
# if counts == 2:
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is NOT prime number!')


#prime number v0.2

# number = int(input('input integer number : '))
# counts = 0  # primenumber 판정용도
#
# for k in range(1, number+1): #2부터 입력된 수 앞까지 반복
#     if number % k == 0:
#         counts = counts + 1
#
# if counts == 0: # counts 증가하지 않았으면 소수
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is NOT prime number!')


#prime number v0.3

number = int(input('input integer number : '))
is_prime = True  # True가 유지되면 소수

for k in range(1, number+1): #2부터 입력된 수 앞까지 반복
    if number % k == 0:
        # counts = counts + 1
        is_prime = False

if is_prime : # is_prime 변수의 True 값이 유지되면 소수
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')
    

    
#prime number v0.4

number = int(input('input integer number : '))
is_prime = True  # True가 유지되면 소수

for k in range(1, number+1): #2부터 입력된 수 앞까지 반복
    if number % k == 0:
        is_prime = False
        break # 첫 번째 약수 발견시 for문 탈출(성능 향상)

if is_prime : # is_prime 변수의 True 값이 유지되면 소수
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number!')    
