# if~elif~else4

print("===== menu =====")
print("1.icecream 1000원 2.coffee 2000원 3.candy 500원\n")

coffee = 2000
ice = 1000
candy = 500
money = int(input("Insert Coin : "))

if money >= coffee:
    print("everything")
elif money < coffee and money >= ice:
    print("ice & candy")
elif money < ice and money >= candy :
    print("candy")
else :
    print("nothing")