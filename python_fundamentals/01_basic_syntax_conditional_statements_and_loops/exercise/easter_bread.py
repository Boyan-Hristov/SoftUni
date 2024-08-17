budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
loaf_price = flour_price + eggs_price + milk_price / 4

coloured_eggs = 0
loaves_made = 0
while budget >= loaf_price:
    loaves_made += 1
    budget -= loaf_price
    coloured_eggs += 3
    if loaves_made % 3 == 0:
        coloured_eggs -= loaves_made - 2

print(f"You made {loaves_made} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
