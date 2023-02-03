# if~elif~else2

shortcut = int(input("단축키를 입력하세요(1 엄마 2 아빠 3 동생) : "))

if shortcut == 1:
    print("엄마 : 010-1234-5678")
elif shortcut == 2:
    print("아빠 : 010-0000-5678")
elif shortcut == 3:
    print("동생 : 010-1234-0000")
else:
    print("단축키가 없습니다.")
