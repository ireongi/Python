# while문으로 구구단 출력하기

# 입력받은 단만 출력
num = 1
dan = int(input('몇 단? : '))
while num < 10:
    print(dan, ' * ', num, '=', dan * num)
    num += 1

# 구구단 전체 출력
dan = 2
while dan < 10:
    num = 1 # while문 밖으로 나가면 dan 증가가 안됨 why?
    while num < 10:
     print("%d * %d = %d" % (dan, num, dan * num))
     num += 1
    dan += 1

