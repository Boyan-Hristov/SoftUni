activation_key = input()
command = input()
while not command == "Generate":
    tokens = command.split(">>>")
    action = tokens[0]
    if action == "Contains":
        substring = tokens[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        flip_to = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        substring_to_flip = activation_key[start_index:end_index]
        flipped_substring = ""
        if flip_to == "Upper":
            flipped_substring = substring_to_flip.upper()
        elif flip_to == "Lower":
            flipped_substring = substring_to_flip.lower()
        activation_key = activation_key.replace(substring_to_flip, flipped_substring)
        print(activation_key)
    elif action == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        substring_to_delete = activation_key[start_index:end_index]
        activation_key = activation_key.replace(substring_to_delete, "")
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")
