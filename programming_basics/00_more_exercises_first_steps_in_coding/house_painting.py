house_height = float(input())
house_width = float(input())
roof_height = float(input())

area_per_liter_green_paint = 3.4
area_per_liter_red_paint = 4.3

front_wall_area = house_height ** 2
back_wall_area = front_wall_area
front_door_area = 1.2 * 2

side_walls_area = house_width * house_height * 2
windows_area = 1.5 ** 2 * 2

front_roof_area = 2 * (house_height * roof_height / 2)
side_roof_area = house_height * house_width * 2

area_needing_green_paint = front_wall_area + back_wall_area + side_walls_area \
    - front_door_area - windows_area
area_needing_red_paint = front_roof_area + side_roof_area

green_paint_needed = area_needing_green_paint / area_per_liter_green_paint
red_paint_needed = area_needing_red_paint / area_per_liter_red_paint

print(f"{green_paint_needed :.2f}")
print(f"{red_paint_needed :.2f}")
