screening_type = input()
rows = int(input())
columns = int(input())

cost_per_seat = 0
if screening_type == "Premiere":
    cost_per_seat = 12.00
elif screening_type == "Normal":
    cost_per_seat = 7.50
elif screening_type == "Discount":
    cost_per_seat = 5

income = rows * columns * cost_per_seat
print(f"{income:.2f} leva")


