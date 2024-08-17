budget = float(input())
season = input()

price_percentage = 0
car_class = ""
type = ""
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        type = "Cabrio"
        price_percentage = 0.35
    elif season == "Winter":
        type = "Jeep"
        price_percentage = 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type = "Cabrio"
        price_percentage = 0.45
    elif season == "Winter":
        type = "Jeep"
        price_percentage = 0.80
else:
    car_class = "Luxury class"
    type = "Jeep"
    price_percentage = 0.90

car_price = budget * price_percentage

print(car_class)
print(f"{type} - {car_price:.2f}")