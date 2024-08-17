age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_sum = 0
for year in range(1, age + 1):
    if year % 2 == 0:
        money_sum += year * 5
        money_sum -= 1
    else:
        money_sum += toy_price

money_left = 0
money_needed = 0
if money_sum >= washing_machine_price:
    money_left = money_sum - washing_machine_price
    print(f"Yes! {money_left :.2f}")
else:
    money_needed = washing_machine_price - money_sum
    print(f"No! {money_needed :.2f}")