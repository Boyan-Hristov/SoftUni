destination = input()

while destination != "End":
    vacation_cost = float(input())
    total_money = 0
    while total_money < vacation_cost:
        money_saved = float(input())
        total_money += money_saved
    print(f"Going to {destination}!")
    destination = input()
