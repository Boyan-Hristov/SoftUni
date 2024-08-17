days = int(input())
hours = int(input())

even_day_odd_hour_fee = 2.50
odd_day_even_hour_fee = 1.25
other_fee = 1

total_fee = 0
daily_fee = 0
flag = False
for day in range(1, days + 2):
    total_fee += daily_fee
    if flag:
        print(f"Day: {day - 1} - {daily_fee:.2f} leva")
    daily_fee = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and not hour % 2 == 0:
            daily_fee += even_day_odd_hour_fee
        elif not day % 2 == 0 and hour % 2 == 0:
            daily_fee += odd_day_even_hour_fee
        else:
            daily_fee += other_fee
        flag = True
print(f"Total: {total_fee:.2f} leva")


