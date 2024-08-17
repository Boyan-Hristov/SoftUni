vacation_cost = float(input())
starting_money = float(input())

saved_money = starting_money
days_spending = 0
days_count = 0

while saved_money < vacation_cost and days_spending < 5:
    command = input()
    money_sum = float(input())
    days_count += 1
    if command == "spend":
        days_spending += 1
        saved_money -= money_sum
        if saved_money < 0:
            saved_money = 0
    elif command == "save":
        saved_money += money_sum
        days_spending = 0

if days_spending == 5:
    print(f"You can't save the money.")
    print(f"{days_count}")
if saved_money >= vacation_cost:
    print(f"You saved the money for {days_count} days.")