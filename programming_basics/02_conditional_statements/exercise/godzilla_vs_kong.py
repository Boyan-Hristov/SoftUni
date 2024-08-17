movie_budget = float(input())
walk_on_number = int(input())
costume_price_per_walk_on = float(input())

decor = movie_budget * 0.10
total_costume_price = costume_price_per_walk_on * walk_on_number

discount = 0
if walk_on_number > 150:
    discount = total_costume_price * 0.10

total_costume_price_with_discount = total_costume_price - discount

expenses = total_costume_price_with_discount + decor

funds_needed = 0
funds_left = 0
if expenses > movie_budget:
    funds_needed = expenses - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {funds_needed:.2f} leva more.")
else:
    funds_left = movie_budget - expenses
    print("Action!")
    print(f"Wingard starts filming with {funds_left:.2f} leva left.")
