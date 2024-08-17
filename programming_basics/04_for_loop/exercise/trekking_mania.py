groups_count = int(input())

mussala_climbers = 0
monblan_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for _ in range(groups_count):
    climbers_count = int(input())
    if climbers_count < 6:
        mussala_climbers += climbers_count
    elif climbers_count < 13:
        monblan_climbers += climbers_count
    elif climbers_count < 26:
        kilimanjaro_climbers += climbers_count
    elif climbers_count < 41:
        k2_climbers += climbers_count
    elif climbers_count >= 41:
        everest_climbers += climbers_count

total_climbers = mussala_climbers + monblan_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers
mussala_climbers_percent = mussala_climbers / total_climbers * 100
monblan_climbers_percent = monblan_climbers / total_climbers * 100
kilimanjaro_climbers_percent = kilimanjaro_climbers / total_climbers * 100
k2_climbers_percent = k2_climbers / total_climbers * 100
everest_climbers_percent = everest_climbers / total_climbers * 100

print(f"{mussala_climbers_percent :.2f}%")
print(f"{monblan_climbers_percent :.2f}%")
print(f"{kilimanjaro_climbers_percent :.2f}%")
print(f"{k2_climbers_percent :.2f}%")
print(f"{everest_climbers_percent :.2f}%")