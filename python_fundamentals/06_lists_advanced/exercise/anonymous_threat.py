strings = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    if command[0] == "merge":
        merged_strings = ""
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(strings) - 1:
            end_index = len(strings) - 1
        for index in range(start_index, end_index + 1):
            merged_strings += strings[index]
    elif command[0] == "divide":
        divide_index = int(command[1])
        partitions_count = int(command[2])
        element = strings[divide_index]
        partition_length = len(element) // partitions_count
        partitions = []
        for current_element_index in range(partitions_count):
            if current_element_index != partitions_count - 1:
                partitions.append(
                    element[current_element_index*partition_length:(current_element_index + 1)*partition_length])
            else:
                partitions.append(element[current_element_index * partition_length:])
        strings[divide_index:divide_index + 1] = partitions
print(" ".join(strings))





