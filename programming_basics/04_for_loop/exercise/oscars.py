actor_name = input()
starting_points = float(input())
judges_count = int(input())

total_points = starting_points
for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    judge_score = len(judge_name) * judge_points / 2
    total_points += judge_score
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points :.1f}!")
        break
if total_points <= 1250.5:
    points_needed = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {points_needed :.1f} more!")