budget = float(input())
season = input()

location = ""
acommodation = ""
price_percentage = 0

if budget <= 1000:
    acommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_percentage = 0.65
    elif season == "Winter":
        location = "Morocco"
        price_percentage = 0.45
elif 1000 < budget <= 3000:
    acommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_percentage = 0.8
    elif season == "Winter":
        location = "Morocco"
        price_percentage = 0.6
else:
    acommodation = "Hotel"
    price_percentage = 0.9
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

stay_cost = budget * price_percentage

print(f"{location} - {acommodation} - {stay_cost:.2f}")