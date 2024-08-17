from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(y) for y in input().split(", ")])

milkshakes = 0
is_done = False

while chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 or milk <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)
        elif milk > 0:
            cups_of_milk.appendleft(milk)
        continue

    if chocolate == milk:
        milkshakes += 1
        if milkshakes == 5:
            is_done = True
            break
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk)

if is_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: ", end="")
    print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")
