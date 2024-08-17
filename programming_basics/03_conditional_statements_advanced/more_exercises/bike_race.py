juniors = int(input())
seniors = int(input())
race_type = input() # "trail", "cross-country", "downhill" or "road"

junior_tax = 0
discount = 0
senior_tax = 0
if race_type == "trail":
    junior_tax = 5.50
    senior_tax = 7
elif race_type == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
    if juniors + seniors >= 50:
        discount = 0.25
elif race_type == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
elif race_type == "road":
    junior_tax = 20
    senior_tax = 21.50

tax_income = (junior_tax * juniors + senior_tax * seniors) * (1 - discount)
expenses = tax_income * 0.05

money_after_expenses = tax_income - expenses

print(f"{money_after_expenses:.2f}")

