change = float(input())

change_as_pennies = int(change * 100)
coins_count = 0

while change_as_pennies > 0:
    if change_as_pennies >= 200:
        change_as_pennies -= 200
    elif change_as_pennies >= 100:
        change_as_pennies -= 100
    elif change_as_pennies >= 50:
        change_as_pennies -= 50
    elif change_as_pennies >= 20:
        change_as_pennies -= 20
    elif change_as_pennies >= 10:
        change_as_pennies -= 10
    elif change_as_pennies >= 5:
        change_as_pennies -= 5
    elif change_as_pennies >= 2:
        change_as_pennies -= 2
    elif change_as_pennies >= 1:
        change_as_pennies -= 1

    coins_count += 1

print(coins_count)