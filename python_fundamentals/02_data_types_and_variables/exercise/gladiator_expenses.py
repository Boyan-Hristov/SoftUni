lost_fights = int(input())
helmet_repair_price = float(input())
sword_repair_price = float(input())
shield_repair_price = float(input())
armour_repair_price = float(input())

helmet_repairs = lost_fights // 2
sword_repairs = lost_fights // 3
shield_repairs = lost_fights // 6
armour_repairs = shield_repairs // 2

total_expenses = helmet_repairs * helmet_repair_price \
    + sword_repairs * sword_repair_price \
    + shield_repairs * shield_repair_price \
    + armour_repairs * armour_repair_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")