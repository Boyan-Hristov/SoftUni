def modify_course(some_command):
    if some_command[0] == "Add":
        if some_command[1] not in schedule:
            schedule.append(some_command[1])
    elif some_command[0] == "Insert":
        if some_command[1] not in schedule:
            schedule.insert(int(some_command[2]), some_command[1])
    elif some_command[0] == "Remove":
        if some_command[1] in schedule:
            schedule.remove(some_command[1])
            if f"{some_command[1]}-Exercise" in schedule:
                schedule.remove(f"{some_command[1]}-Exercise")
    elif some_command[0] == "Swap":
        first_lesson = some_command[1]
        second_lesson = some_command[2]
        first_exercise = f"{first_lesson}-Exercise"
        second_exercise = f"{second_lesson}-Exercise"
        if first_lesson in schedule and second_lesson in schedule:
            first_lesson_index = schedule.index(first_lesson)
            second_lesson_index = schedule.index(second_lesson)
            schedule[first_lesson_index], schedule[second_lesson_index] = \
                schedule[second_lesson_index], schedule[first_lesson_index]
            if first_exercise in schedule:
                schedule.remove(first_exercise)
                schedule.insert(second_lesson_index + 1, first_exercise)
            if second_exercise in schedule:
                schedule.remove(second_exercise)
                schedule.insert(first_lesson_index + 1, second_exercise)
    elif some_command[0] == "Exercise":
        exercise = f"{some_command[1]}-Exercise"
        if some_command[1] not in schedule:
            schedule.append(some_command[1])
            schedule.append(exercise)
        else:
            if exercise not in schedule:
                lesson_index = schedule.index(some_command[1])
                schedule.insert(lesson_index + 1, exercise)
    return schedule


schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    command_info = command.split(":")
    modify_course(command_info)

for index in range(len(schedule)):
    print(f"{index + 1}.{schedule[index]}")
