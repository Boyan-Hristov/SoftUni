from math import ceil

series_name = input()
episode_length = int(input())
break_time = int(input())

LUNCH_TIME_TO_BREAK_TIME_RATIO = 0.125
RECREATION_TIME_TO_BREAK_TIME_RATIO = 0.25

lunch_time = break_time * LUNCH_TIME_TO_BREAK_TIME_RATIO
recreation_time = break_time * RECREATION_TIME_TO_BREAK_TIME_RATIO

free_time = break_time - lunch_time - recreation_time

time_left = 0
time_needed = 0
if free_time >= episode_length:
    time_left = free_time - episode_length
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    time_needed = episode_length - free_time
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_needed)} more minutes.")
