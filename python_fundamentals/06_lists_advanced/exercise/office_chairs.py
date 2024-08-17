number_of_rooms = int(input())
are_enough = True
chairs = 0
visitors = 0
for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs_available = len(chairs_and_visitors[0])
    number_of_visitors = int(chairs_and_visitors[1])
    if chairs_available < number_of_visitors:
        are_enough = False
        chairs_needed = number_of_visitors - chairs_available
        print(f"{chairs_needed} more chairs needed in room {room}")
    else:
        chairs += chairs_available
        visitors += number_of_visitors

if are_enough:
    free_chairs = chairs - visitors
    print(f"Game On, {free_chairs} free chairs left")
