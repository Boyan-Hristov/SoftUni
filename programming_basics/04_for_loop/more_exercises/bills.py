months = int(input())

total_expenses = 0
total_electricity = 0
total_water = 0
total_internet = 0
total_others = 0
for month in range(months):
    electricity = float(input())
    water = 20
    internet = 15
    other_expenses = (electricity + water + internet) * 0.2 + electricity + water + internet

    monthly_expenses = electricity + water + internet + other_expenses

    total_expenses += monthly_expenses
    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_others += other_expenses

average_expenses = total_expenses / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")



