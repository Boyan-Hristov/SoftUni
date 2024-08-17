number = int(input())
bonus = 0
extra_bonus = 0

if number <= 100:
    bonus = 5
elif number <= 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1

if number % 2 == 0:
    extra_bonus = 1
if number % 10 == 5:
    extra_bonus = extra_bonus + 2

bonus_sum = bonus + extra_bonus
total_sum = number + bonus + extra_bonus

print(bonus_sum)
print(total_sum)
