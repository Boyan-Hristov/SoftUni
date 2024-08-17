days = int(input())
room_type = input()
review = input()

room_for_one_person_price = 18
apartment_price = 25
president_apartment_price = 35
nights = days - 1

discount = 0
room_price = 0
if room_type == "room for one person":
    room_price = 18
    discount = 0
elif room_type == "apartment":
    room_price = 25
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
elif room_type == "president apartment":
    room_price = 35
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20

total_price_with_discount = nights * room_price * (1 - discount)

final_price = 0
if review == "positive":
    final_price = total_price_with_discount + (total_price_with_discount * 0.25)
elif review == "negative":
    final_price = total_price_with_discount * 0.90

print(f"{final_price :.2f}")