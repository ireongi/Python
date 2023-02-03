# Break & Continue

# Break
age = 26
while True:
    if age > 19:
        break
    print(f'{age}살, 미성년자입니다.')
print(f'{age}살, 성인입니다.')

# Continue
age2 = 10
while True:
    if age2 < 19:
        print(f'{age2}살, 미성년자입니다.')
        age2 += 1
        continue
print(f'{age2}살, 성인입니다.')