target = int(input())

profit = 0
while profit < target:
    command = input()
    if command == "closed":
        break
    elif command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            profit += 15
        elif haircut_type == "ladies":
            profit += 20
        elif haircut_type == "kids":
            profit += 10
    elif command == "color":
        color_type = input()
        if color_type == "touch up":
            profit += 20
        elif color_type == "full color":
            profit += 30

money_needed = 0
if profit >= target:
    print(f"You have reached your target for the day!" )
else:
    money_needed = target - profit
    print(f"Target not reached! You need {money_needed}lv. more.")
print(f"Earned money: {profit}lv.")