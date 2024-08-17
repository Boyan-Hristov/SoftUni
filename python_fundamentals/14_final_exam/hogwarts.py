spell = input()
command = input()
while not command == "Abracadabra":
    tokens = command.split()
    action = tokens[0]
    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index, letter = int(tokens[1]), tokens[2]
        if index in range(len(spell)):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        first_substring, second_substring = tokens[1], tokens[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif action == "Alteration":
        substring = tokens[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")
    command = input()
