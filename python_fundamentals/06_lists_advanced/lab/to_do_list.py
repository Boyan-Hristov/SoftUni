to_do_list = []
note = input()

while not note == "End":
    to_do_list.append(note)
    note = input()

sorted_to_do_list = sorted(to_do_list, key=lambda task: int(task.split("-")[0]))
final_list = [task.split("-")[1] for task in sorted_to_do_list]
print(final_list)
