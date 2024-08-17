dancers_count = int(input())
points_amount = float(input())
season = input()
venue = input()

prize = 0
expenses = 0

if season == "summer":
    if venue == "Bulgaria":
        prize = dancers_count * points_amount
        expenses = prize * 0.05
    elif venue == "Abroad":
        prize = dancers_count * points_amount
        prize += prize * 0.5
        expenses = prize * 0.1
elif season == "winter":
    if venue == "Bulgaria":
        prize = dancers_count * points_amount
        expenses = prize * 0.08
    elif venue == "Abroad":
        prize = dancers_count * points_amount
        prize += prize * 0.5
        expenses = prize * 0.15

money_after_expenses = prize - expenses
charity = money_after_expenses * 0.75
total_money_after_charity = money_after_expenses - charity
money_per_dancer = total_money_after_charity / dancers_count

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")