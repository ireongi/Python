# 입력받은 값과 설정 값이 같은지 검사하는 함수

name = "reong"
birth_month = 6


def test(input_name, input_birth_month):
    if input_name == name:
        print("성명 동일")
    else:
        print("성명 상이")
    if input_birth_month == birth_month:
        print("탄생 월 동일")
    else:
        print("탄생 월 상이")


user_name = input("성명 입력 : ")
user_birth_month = int(input("탄생 월 입력 : "))

test(user_name, user_birth_month)


