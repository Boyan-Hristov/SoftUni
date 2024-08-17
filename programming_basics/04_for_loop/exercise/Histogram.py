numbers = int(input())

p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0

for _ in range(numbers):
    current_number = int(input())
    if current_number < 200:
        p_1 += 1
    elif current_number < 400:
        p_2 += 1
    elif current_number < 600:
        p_3 += 1
    elif current_number < 800:
        p_4 += 1
    elif current_number >= 800:
        p_5 += 1

p_1_percent = p_1 / numbers * 100
p_2_percent = p_2 / numbers * 100
p_3_percent = p_3 / numbers * 100
p_4_percent = p_4 / numbers * 100
p_5_percent = p_5 / numbers * 100

print(f"{p_1_percent :.2f}%")
print(f"{p_2_percent :.2f}%")
print(f"{p_3_percent :.2f}%")
print(f"{p_4_percent :.2f}%")
print(f"{p_5_percent :.2f}%")
