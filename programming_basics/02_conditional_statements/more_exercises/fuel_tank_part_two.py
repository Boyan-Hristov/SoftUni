fuel_type = input()
fuel_amount = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
lpg_price = 0.93

gasoline_club_discount_per_liter = 0.18
diesel_club_discount_per_liter = 0.12
lpg_club_discount_per_liter = 0.08

fuel_price = 0
extra_discount = 0
if fuel_type == "Gasoline":
    if club_card == "Yes":
        gasoline_price -= gasoline_club_discount_per_liter
    if 20 <= fuel_amount <= 25:
        extra_discount = 0.08
    elif fuel_amount > 25:
        extra_discount = 0.1
    fuel_price = gasoline_price * fuel_amount * (1 - extra_discount)
elif fuel_type == "Diesel":
    if club_card == "Yes":
        diesel_price -= diesel_club_discount_per_liter
    if 20 <= fuel_amount <= 25:
        extra_discount = 0.08
    elif fuel_amount > 25:
        extra_discount = 0.1
    fuel_price = diesel_price * fuel_amount * (1 - extra_discount)
elif fuel_type == "Gas":
    if club_card == "Yes":
        lpg_price -= lpg_club_discount_per_liter
    if 20 <= fuel_amount <= 25:
        extra_discount = 0.08
    elif fuel_amount > 25:
        extra_discount = 0.1
    fuel_price = lpg_price * fuel_amount * (1 - extra_discount)

print(f"{fuel_price:.2f} lv.")