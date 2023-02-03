# loop

# 무한 루프
loop = 0
while loop < 5:
    print('*')
    break # 지우면 무한루프


# 정수 입력 받아 누적 값 구하기

result = 0
integer_num = 0
while True:
    integer_num = int(input('정수 입력 : '))
    result += integer_num
    print(f'누적된 숫자는 : {result}입니다.')
