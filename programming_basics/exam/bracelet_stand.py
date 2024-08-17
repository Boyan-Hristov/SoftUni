days = 5
pocket_money_per_day = float(input())
profit_per_day = float(input())
total_expenses = float(input())
present_price = float(input())

total_pocket_money = pocket_money_per_day * days
total_profit = profit_per_day * days
total_money_saved = total_pocket_money + total_profit

total_money = total_money_saved - total_expenses

if total_money >= present_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    money_needed = present_price - total_money
    print(f"Insufficient money: {money_needed:.2f} BGN.")

