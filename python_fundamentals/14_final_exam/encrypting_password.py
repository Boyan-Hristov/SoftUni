import re

number_of_passwords = int(input())
pattern = r"(.)+>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})<\1+"
for i in range(number_of_passwords):
    password = input()
    encrypted_password = ""
    matches = re.findall(pattern, password)
    if matches:
        for match in matches:
            for index in range(len(match)):
                if index != 0:
                    encrypted_password += match[index]
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
