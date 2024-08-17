hour = int(input())
minutes = int(input())
INCREMENT = 15
MINUTES_ABS = 60
HOUR_ABS = 24

minutes_plus_increment = minutes + INCREMENT

if minutes_plus_increment >= MINUTES_ABS:
    hour += +1
    minutes_plus_increment = minutes_plus_increment - MINUTES_ABS

if hour >= HOUR_ABS:
    hour = HOUR_ABS - hour

print(f"{hour}:{minutes_plus_increment:02d}")