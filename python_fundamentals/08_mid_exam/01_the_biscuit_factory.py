from math import floor

biscuits_per_worker_per_day = int(input())
workers = int(input())
competition_production = int(input())

biscuits_produced = 0
for day in range(1, 31):
    biscuits_production_per_day = biscuits_per_worker_per_day * workers
    if day % 3 == 0:
        biscuits_production_per_day *= 0.75
    biscuits_produced += floor(biscuits_production_per_day)

production_difference = abs(biscuits_produced - competition_production)
production_difference_percent = production_difference/competition_production * 100

print(f"You have produced {biscuits_produced} biscuits for the past month.")
if biscuits_produced > competition_production:
    print(f"You produce {production_difference_percent:.2f} percent more biscuits.")
else:
    print(f"You produce {production_difference_percent:.2f} percent less biscuits.")

