# If~else2

id = "reong"
pw = "1234"

userID = input("ID : ")
userPW = input("PW : ")

if id == userID :
    if pw == userPW :
        print("로그인 되었습니다.")
    else:
        print("사용자 비밀번호가 틀렸습니다.")
else:
    print("사용자 아이디가 틀렸습니다.")