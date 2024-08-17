distance = int(input())
time_of_day = input()

taxi_starting_fee = 0.7
taxi_day_rate = 0.79
taxi_night_rate = 0.9

bus_rate = 0.09
bus_minimal_distance = 20

train_rate = 0.06
train_minimal_distance = 100

cheapest_fee = 0
bus_fee = distance * bus_rate
train_fee = distance * train_rate
taxi_fee = 0

if time_of_day == "day":
    taxi_fee = taxi_starting_fee + distance * taxi_day_rate
elif time_of_day == "night":
    taxi_fee = taxi_starting_fee + distance * taxi_night_rate

if distance < bus_minimal_distance:
    cheapest_fee = taxi_fee
elif distance < train_minimal_distance:
    cheapest_fee = bus_fee
elif distance >= train_minimal_distance:
    cheapest_fee = train_fee

print(f"{cheapest_fee:.2f}")