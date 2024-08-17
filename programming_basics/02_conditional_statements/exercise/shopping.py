budget = float(input())
number_of_graphics_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

graphics_card_price = 250
graphics_cards_cost = number_of_graphics_cards * graphics_card_price

processors_price = graphics_cards_cost * 0.35
processors_cost = number_of_processors * processors_price

ram_price = graphics_cards_cost * 0.10
ram_cost = number_of_ram * ram_price

total_cost = graphics_cards_cost + processors_cost + ram_cost

discount = 0
if number_of_graphics_cards > number_of_processors:
    discount = total_cost * 0.15

total_cost_with_discount = total_cost - discount

money_left = 0
money_needed = 0
if budget >= total_cost_with_discount:
    money_left = budget - total_cost_with_discount
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_cost_with_discount - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")





