lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

full_capacity = lenght * width * height / 1000
filled_capacity = full_capacity * percent / 100
free_capacity = full_capacity - filled_capacity

print(free_capacity)