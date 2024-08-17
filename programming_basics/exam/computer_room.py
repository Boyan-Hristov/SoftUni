month = input()
hours = int(input())
people_count = int(input())
time_of_day = input()

price_per_hour = 0
if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price_per_hour = 10.5
    elif time_of_day == "night":
        price_per_hour = 8.4
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price_per_hour = 12.60
    elif time_of_day == "night":
        price_per_hour = 10.20

discount_one = 0
discount_two = 0
if people_count >= 4:
    discount_one = 0.1
    price_per_hour = price_per_hour * (1 - discount_one)
if hours >= 5:
    discount_two = 0.5
    price_per_hour = price_per_hour * (1 - discount_two)


total_cost = price_per_hour * people_count * hours

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")

