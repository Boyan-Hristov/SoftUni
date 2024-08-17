stadium_capacity = int(input())
audience = int(input())

sector_A_fans = 0
sector_B_fans = 0
sector_V_fans = 0
sector_G_fans = 0

for fan in range(audience):
    sector = input()
    if sector == "A":
        sector_A_fans += 1
    elif sector == "B":
        sector_B_fans += 1
    elif sector == "V":
        sector_V_fans += 1
    elif sector == "G":
        sector_G_fans += 1

sector_A_fans_percent = sector_A_fans / audience * 100
sector_B_fans_percent = sector_B_fans / audience * 100
sector_V_fans_percent = sector_V_fans / audience * 100
sector_G_fans_percent = sector_G_fans / audience * 100
total_fans_percent = audience / stadium_capacity * 100

print(f"{sector_A_fans_percent:.2f}%")
print(f"{sector_B_fans_percent:.2f}%")
print(f"{sector_V_fans_percent:.2f}%")
print(f"{sector_G_fans_percent:.2f}%")
print(f"{total_fans_percent:.2f}%")
