# if~elif~else4

print("===== 자판기 메뉴 =====")
print("1.음료 1000원 2.과자 2000원 3.껌 500원\n")

cracker = 2000
drink = 1000
ggum = 500
money = int(input("Insert Coin : "))

if money >= cracker:
    print("모두 구매할 수 있습니다.")
elif money < cracker and money >= drink:
    print("음료와 껌을 구매할 수 있습니다.")
elif money < drink and money >= ggum :
    print("껌을 구매할 수 있습니다.")
else :
    print("아무걳도 구매할 수 없습니다.")