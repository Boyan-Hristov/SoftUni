season = input()
kilometers_per_month = float(input())

months_in_season = 4

pay_per_kilometer = 0
if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        pay_per_kilometer = 0.75
    elif season == "Summer":
        pay_per_kilometer = 0.9
    elif season == "Winter":
        pay_per_kilometer = 1.05
elif 5000 < kilometers_per_month <= 10_000:
    if season == "Spring" or season == "Autumn":
        pay_per_kilometer = 0.95
    elif season == "Summer":
        pay_per_kilometer = 1.10
    elif season == "Winter":
        pay_per_kilometer = 1.25
elif 10_000 < kilometers_per_month <= 20_000:
    pay_per_kilometer = 1.45

taxes = 0.1

profit = kilometers_per_month * months_in_season * pay_per_kilometer * (1 - taxes)

print(f"{profit:.2f}")