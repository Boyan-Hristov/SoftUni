season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

night_price = 0
sport = ""
discount = 0

if season == "Winter":
    if group_type == "boys":
        night_price = 9.60
        sport = "Judo"
    elif group_type == "girls":
        night_price = 9.60
        sport = "Gymnastics"
    elif group_type == "mixed":
        night_price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        night_price = 7.20
        sport = "Tennis"
    elif group_type == "girls":
        night_price = 7.20
        sport = "Athletics"
    elif group_type == "mixed":
        night_price = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        night_price = 15
        sport = "Football"
    elif group_type == "girls":
        night_price = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        night_price = 20
        sport = "Swimming"

if 10 <= students_count < 20:
    discount = 0.05
elif 20 <= students_count < 50:
    discount = 0.15
elif 50 <= students_count:
    discount = 0.5

total_nights_price = night_price * nights_count * students_count * (1 - discount)

print(f"{sport} {total_nights_price:.2f} lv.")