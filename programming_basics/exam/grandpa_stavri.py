days = int(input())

total_amount = 0
total_degrees = 0
for _ in range(days):
    rakia_amount = float(input())
    rakia_degrees = float(input())
    total_amount += rakia_amount
    total_degrees += rakia_degrees * rakia_amount

degrees = total_degrees / total_amount

print(f"Liter: {total_amount:.2f}")
print(f"Degrees: {degrees:.2f}")

if degrees < 38:
    print("Not good, you should baking!")
elif 38 <= degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")

