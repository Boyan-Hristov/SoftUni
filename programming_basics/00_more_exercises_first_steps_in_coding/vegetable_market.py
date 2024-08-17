BGN_TO_EUR = 1.94

vegetable_price = float(input())
fruit_price = float(input())
vegetable_weight = float(input())
fruit_weight = float(input())

harvest = vegetable_price * vegetable_weight + fruit_price * fruit_weight
harvest_in_eur = harvest / BGN_TO_EUR

print(f"{harvest_in_eur:.2f}")
