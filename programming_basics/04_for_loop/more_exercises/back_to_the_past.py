money_inherited = float(input())
target_year = int(input())

current_year = 1800
years_remaining = target_year - current_year
current_age = 18
total_money_spent = 0
money_spent_if_year_is_even = 12_000

for year in range(years_remaining + 1):
    if current_year % 2 == 0:
        total_money_spent += money_spent_if_year_is_even
    else:
        total_money_spent += money_spent_if_year_is_even + 50 * current_age
    current_year += 1
    current_age += 1

if total_money_spent <= money_inherited:
    money_left = money_inherited - total_money_spent
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_needed = total_money_spent - money_inherited
    print(f"He will need {money_needed:.2f} dollars to survive.")


