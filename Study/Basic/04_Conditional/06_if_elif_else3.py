# if~elif~else3

month = int(input("월 : "))

if month == 12 or month < 3 and month > 0: #12월, 1~2월
    print("winter")
elif month > 2 and month < 6: #3~5월
    print("spring")
elif month > 5 and month < 9: #6~8월
    print("summer")
elif month > 8 and month < 12: #9~11월
    print("fall")
else:
    print("error")