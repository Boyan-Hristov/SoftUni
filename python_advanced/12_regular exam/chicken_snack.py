from collections import deque

money_sequence = [int(x) for x in input().split()]
prices = deque([int(y) for y in input().split()])

foods_eaten = 0

while money_sequence and prices:
    money = money_sequence.pop()
    price = prices.popleft()

    if money == price:
        foods_eaten += 1
    elif money > price:
        foods_eaten += 1
        change = money - price
        if money_sequence:
            money_sequence.append(money_sequence.pop() + change)

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
elif 1 < foods_eaten < 4:
    print(f"Henry ate: {foods_eaten} foods.")
elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")
elif foods_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
