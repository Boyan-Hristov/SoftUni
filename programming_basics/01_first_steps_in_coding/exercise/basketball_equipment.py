annual_training_fee = int(input())

basketball_shoes = annual_training_fee - annual_training_fee * 0.4
basketball_jersey = basketball_shoes - basketball_shoes * 0.2
basketball_ball = basketball_jersey * 1/4
basketball_accessories = basketball_ball * 1/5

total_expenses = annual_training_fee \
                 + basketball_shoes \
                 + basketball_jersey \
                 + basketball_ball \
                 + basketball_accessories

print(total_expenses)

