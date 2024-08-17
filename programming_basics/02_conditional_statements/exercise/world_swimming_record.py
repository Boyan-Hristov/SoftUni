from math import floor

swimming_record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

number_of_meters_causing_resistance = 15
water_resistance_per_15_meters = 12.5
total_number_of_meters_causing_resistance = distance_in_meters / number_of_meters_causing_resistance
extra_seconds = floor(total_number_of_meters_causing_resistance) * water_resistance_per_15_meters

time_in_seconds = distance_in_meters * seconds_per_meter
total_time_in_seconds = time_in_seconds + extra_seconds

delay = 0
if total_time_in_seconds < swimming_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_in_seconds:.2f} seconds.")
else:
    delay = total_time_in_seconds - swimming_record_in_seconds
    print(f"No, he failed! He was {delay:.2f} seconds slower.")





