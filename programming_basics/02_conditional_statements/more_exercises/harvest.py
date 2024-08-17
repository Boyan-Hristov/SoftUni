from math import floor
from math import ceil

vineyard_area = int(input())
grapes_per_square_meter = float(input())
wine_liters_needed = int(input())
workers_count = int(input())

percentage_of_harvest_for_wine = 0.4
grapes_kilogram_per_liter_wine = 2.5

harvest_available = vineyard_area * percentage_of_harvest_for_wine
grapes_kilograms = harvest_available * grapes_per_square_meter
liters_of_wine = grapes_kilograms / grapes_kilogram_per_liter_wine

wine_needed = wine_liters_needed - liters_of_wine
wine_left = liters_of_wine - wine_liters_needed
wine_per_worker = wine_left / workers_count
if liters_of_wine < wine_liters_needed:
    print(f"It will be a tough winter! More {floor(wine_needed)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(liters_of_wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")