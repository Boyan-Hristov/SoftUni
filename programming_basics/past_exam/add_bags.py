price_above_twenty_kg = float(input())
weight = float(input())
days = int(input())
luggage_count = int(input())
luggage_cost = 0

if weight > 20:
    luggage_cost = price_above_twenty_kg
elif 10 <= weight <= 20:
    luggage_cost = price_above_twenty_kg * 0.5
elif weight < 10:
    luggage_cost = price_above_twenty_kg * 0.2

if days > 30:
    luggage_cost *= 1.1
elif 7 <= days <= 30:
    luggage_cost *= 1.15
elif days < 7:
    luggage_cost *= 1.4

total_luggage_cost = luggage_cost * luggage_count

print(f"The total price of bags is: {total_luggage_cost:.2f} lv.")