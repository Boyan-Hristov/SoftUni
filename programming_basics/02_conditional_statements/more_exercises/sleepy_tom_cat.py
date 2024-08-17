work_day_play_time = 63
day_off_play_time = 127
days_per_year = 365
play_time_norm = 30_000

days_off = int(input())
work_days = days_per_year - days_off
total_play_time = work_days * work_day_play_time + days_off * day_off_play_time

difference = abs(play_time_norm - total_play_time)
hours = difference // 60
minutes = difference % 60

if play_time_norm < total_play_time:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")