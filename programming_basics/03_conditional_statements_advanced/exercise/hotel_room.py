month = input()
nights = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0
studio_discount = 0
apartment_discount = 0
if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < nights <= 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.3

elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights > 14:
        studio_discount = 0.2

elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights > 14:
    apartment_discount = 0.1

total_cost_for_studio = studio_price_per_night * nights * (1 - studio_discount)
total_cost_for_apartment = apartment_price_per_night * nights * (1 - apartment_discount)

print(f"Apartment: {total_cost_for_apartment:.2f} lv.")
print(f"Studio: {total_cost_for_studio:.2f} lv.")




