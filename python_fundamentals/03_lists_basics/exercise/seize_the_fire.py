fire_levels = input()
water_available = int(input())

fire_levels_list = fire_levels.split("#")

effort_needed = 0.25
total_effort = 0
total_fire = 0
cells_put_out = []
for fire in fire_levels_list:
    current_fire_list = fire.split(" ")
    cell_value = int(current_fire_list[2])
    if water_available >= cell_value:
        if "High" in fire:
            if 81 <= cell_value <= 125:
                water_available -= cell_value
                total_effort += cell_value * effort_needed
                total_fire += cell_value
                cells_put_out.append(cell_value)
            else:
                continue
        elif "Medium" in fire:
            if 51 <= cell_value <= 80:
                water_available -= cell_value
                total_effort += cell_value * effort_needed
                total_fire += cell_value
                cells_put_out.append(cell_value)
            else:
                continue
        elif "Low" in fire:
            if 1 <= cell_value <= 50:
                water_available -= cell_value
                total_effort += cell_value * effort_needed
                total_fire += cell_value
                cells_put_out.append(cell_value)
            else:
                continue

print("Cells:")
for i in range(len(cells_put_out)):
    print(f" - {cells_put_out[i]}")
print(f"Effort: {total_effort:.2f}\n")
print(f"Total Fire: {total_fire}")
