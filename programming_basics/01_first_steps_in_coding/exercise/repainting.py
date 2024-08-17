NYLON = 1.50
PAINT = 14.50
SOLUTION = 5.00

bags = 0.40

nylon_needed = int(input())
paint_needed = int(input())
solution_amount = int(input())
hours_needed = int(input())

nylon_backup = nylon_needed + 2
paint_backup = paint_needed + paint_needed * 10 / 100

materials_price = nylon_backup * NYLON \
                  + paint_backup * PAINT \
                  + solution_amount * SOLUTION \
                  + bags
workers_per_hour = materials_price * 30 / 100
workers_price = workers_per_hour * hours_needed

total_price = materials_price + workers_price

print(total_price)