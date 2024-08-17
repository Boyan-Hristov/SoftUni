ciphered_message = input().split()
deciphered_message = ""
for element in ciphered_message:
    element_list = list(element)
    digits = []
    for character in element_list:
        if character.isdigit():
            digits += character
    element_list = [element for element in element_list if element not in digits]
    number = int("".join(digits))
    element_list.insert(0, chr(number))
    element_list[1], element_list[-1] = element_list[-1], element_list[1]
    deciphered_message += f"{''.join(element_list)} "
print(deciphered_message)
