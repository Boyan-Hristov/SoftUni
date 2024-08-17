hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_exam_in_minutes = hour_of_exam * 60 + minutes_of_exam
time_of_arrival_in_minutes = hour_of_arrival * 60 + minutes_of_arrival

difference = time_of_arrival_in_minutes - time_of_exam_in_minutes
if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm:02d} hours after the start")
elif difference >= -30:
    print("On time")
    if difference != 0:
        print(f"{abs(difference)} minutes before the start")
else:
    print("Early")
    if difference > -60:
        print(f"{abs(difference)} minutes before the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm:02d} hours before the start")
