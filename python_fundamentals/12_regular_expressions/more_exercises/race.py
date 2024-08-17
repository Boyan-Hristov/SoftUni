import re

participants_list = input().split(", ")
command = input()
participants_dict = {}
letters_pattern = r"[A-Za-z]+"
digits_pattern = r"\d"
while command != "end of race":
    letter_matches = re.findall(letters_pattern, command)
    digit_matches = re.findall(digits_pattern, command)
    name = ("".join(letter_matches))
    distance = 0
    for digit in digit_matches:
        distance += int(digit)
    if name in participants_list:
        if name in participants_dict.keys():
            participants_dict[name] += distance
        else:
            participants_dict[name] = distance
    command = input()

participants_dict = dict(sorted(participants_dict.items(), key=lambda x: -x[1]))
place = 1
for participant in participants_dict.keys():
    if place > 3:
        break
    if place == 1:
        print(f"1st place: {participant}")
    elif place == 2:
        print(f"2nd place: {participant}")
    elif place == 3:
        print(f"3rd place: {participant}")
    place += 1
