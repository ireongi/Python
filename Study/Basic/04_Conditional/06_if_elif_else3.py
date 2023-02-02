# if~elif~else3

month = int(input("월을 입력하세요 : "))

if month == 12 or month < 3 and month > 0: #12월, 1~2월
    print("겨울")
elif month > 2 and month < 6: #3~5월
    print("봄")
elif month > 5 and month < 9: #6~8월
    print("봄")
elif month > 8 and month < 12: #9~11월
    print("가을입니다")
else:
    print("입력값이 잘못되었습니다.")