PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

DISCOUNT_FOR_MORE_THAN_50_ITEMS = 0.25
RENT_RATE = 0.10

vacation_price = float(input())
puzzle_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())


total_amount = puzzle_amount + talking_doll_amount + teddy_bear_amount + minion_amount + truck_amount

discount = 0
if total_amount >= 50:
    discount = 0.25

total_revenue = puzzle_amount * PUZZLE_PRICE + talking_doll_amount * TALKING_DOLL_PRICE \
                    + teddy_bear_amount * TEDDY_BEAR_PRICE + minion_amount * MINION_PRICE \
                    + truck_amount * TRUCK_PRICE


profit = total_revenue * (1 - discount)
rent = profit * RENT_RATE

money_for_vacation = profit - rent
money_left = money_for_vacation - vacation_price
money_needed = vacation_price - money_for_vacation

if money_for_vacation >= vacation_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")
