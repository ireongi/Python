# If~else2

id = "reong"
pw = "1234"

userID = input("ID : ")
userPW = input("PW : ")

if id == userID :
    if pw == userPW :
        print("로그인")
    else:
        print("PW error")
else:
    print("ID error")