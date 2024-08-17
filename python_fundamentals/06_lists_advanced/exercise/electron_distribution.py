number_of_electrons = int(input())
filled_shells = []
current_shell = 1
electrons_in_shell = 0
while number_of_electrons > 0:
    electrons_in_shell = 0
    while electrons_in_shell < 2 * current_shell ** 2:
        if number_of_electrons == 0:
            break
        electrons_in_shell += 1
        number_of_electrons -= 1
    filled_shells.append(electrons_in_shell)
    current_shell += 1
print(filled_shells)
