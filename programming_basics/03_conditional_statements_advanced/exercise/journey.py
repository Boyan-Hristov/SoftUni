budget = float(input())
season = input() # summer or winter

accommodation_cost = 0
destination = ""
accommodation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        accommodation_cost = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        accommodation_cost = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        accommodation_cost = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        accommodation_cost = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    accommodation_cost = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {accommodation_cost :.2f}")
