command = input()

steps_goal = 10_000
total_steps = 0
current_steps = 0
is_goal_reached = False

while not command == "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= steps_goal:
        is_goal_reached = True
        break
    command = input()

if command == "Going home":
    command = input()
    current_steps = int(command)
    total_steps += current_steps
if total_steps >= steps_goal:
    is_goal_reached = True

if is_goal_reached:
    extra_steps = total_steps - steps_goal
    print(f"Goal reached! Good job!")
    print(f"{extra_steps} steps over the goal!")
else:
    steps_needed = steps_goal - total_steps
    print(f"{steps_needed} more steps to reach goal.")
