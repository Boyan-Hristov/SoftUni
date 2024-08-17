stack = [int(digit) for digit in input().split()]
rack_capacity = int(input())

clothes_sum = 0
racks_used = 0

for i in range(len(stack)):
    cloth_value = stack.pop()
    clothes_sum += cloth_value
    if clothes_sum == rack_capacity:
        clothes_sum = 0
        racks_used += 1
    elif clothes_sum > rack_capacity:
        clothes_sum = 0
        clothes_sum += cloth_value
        racks_used += 1

if clothes_sum > 0:
    racks_used += 1

print(racks_used)
