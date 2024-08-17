from math import floor

tournaments_count = int(input())
starting_points = int(input())

points_won = 0
place = ""
tournaments_won = 0
for _ in range(tournaments_count):
    place = input()
    if place == "W":
        points_won += 2000
        tournaments_won += 1
    elif place == "F":
        points_won += 1200
    elif place == "SF":
        points_won += 720

total_points = starting_points + points_won
points_average = points_won / tournaments_count
tournaments_won_percent = tournaments_won / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(points_average)}")
print (f"{tournaments_won_percent :.2f}%")


