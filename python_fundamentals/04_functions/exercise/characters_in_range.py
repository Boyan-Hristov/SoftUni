first_character = input()
second_character = input()


def missing_characters(char1, char2):
    first_character_as_number = ord(char1)
    second_character_as_number = ord(char2)
    missing_in_range_list = []
    for number in range(first_character_as_number + 1, second_character_as_number):
        missing_in_range_list.append(chr(number))
    missing_in_range = " ".join(missing_in_range_list)
    return missing_in_range


print(missing_characters(first_character, second_character))

