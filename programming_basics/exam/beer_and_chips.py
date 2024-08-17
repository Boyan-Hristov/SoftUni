from math import ceil

name = input()
budget = float(input())
beers = int(input())
chips_packs = int(input())

beer_price = 1.2

beers_cost = beers * beer_price

chips_pack_price = beers_cost * 0.45

chips_packs_cost = chips_packs * chips_pack_price
final_chips_packs_cost = ceil(chips_packs_cost)

total_cost = beers_cost + final_chips_packs_cost

money_left = 0
money_needed = 0
if budget >= total_cost:
    money_left = budget - total_cost
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total_cost - budget
    print(f"{name} needs {money_needed:.2f} more leva!")