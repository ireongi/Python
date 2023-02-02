# if~elif~else4

point = int(input("점수를 입력하세요 : "))

if point <= 100 and point > 90 :
    print('학점 : A')
elif point <= 90 and point > 80 :
    print('학점 : B')
elif point <= 80 and point > 70:
    print('학점 : C')
elif point <= 70 and point > 60:
    print('학점 : D')
elif point <= 60 and point > 0:
    print('학점 : F')
else:
    print("입력값이 잘못되어있습니다.")