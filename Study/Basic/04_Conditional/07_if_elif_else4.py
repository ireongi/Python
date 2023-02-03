# if~elif~else4

point = int(input("점수를 입력 : "))

if point <= 100 and point > 90 :
    print('A')
elif point <= 90 and point > 80 :
    print('B')
elif point <= 80 and point > 70:
    print('C')
elif point <= 70 and point > 60:
    print('D')
elif point <= 60 and point > 0:
    print('F')
else:
    print("error")