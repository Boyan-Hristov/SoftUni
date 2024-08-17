budget = int(input())
command = input()
is_enough = True
product_price = 0
while command != "End":
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        is_enough = False
        break
    command = input()
if is_enough:
    print("You bought everything needed.")