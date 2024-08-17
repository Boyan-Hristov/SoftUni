import math

magnolia_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolia_cost = 3.25
hyacinth_cost = 4
rose_cost = 3.5
cactus_cost = 8
tax_rate = 0.05

total_money = magnolia_cost * magnolia_count \
    + hyacinth_cost * hyacinth_count \
    + rose_cost * roses_count \
    + cactus_cost * cactus_count

taxes = total_money * tax_rate
money_after_taxes = total_money - taxes

money_left = 0
money_needed = 0
if money_after_taxes >= present_price:
    money_left = money_after_taxes - present_price
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    money_needed = present_price - money_after_taxes
    print(f"She will have to borrow {math.ceil(money_needed)} leva.")
