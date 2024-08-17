password_as_string = input()


def valid_password(password):
    is_length_valid = True
    is_chars_and_digits = True
    is_digits_valid = True
    if not 6 <= len(password) <= 10:
        is_length_valid = False

    digits = 0
    for character in password:
        if character.isalpha() or character.isdigit():
            if character.isdigit():
                digits += 1
        else:
            is_chars_and_digits = False
            break

    if digits < 2:
        is_digits_valid = False

    if is_length_valid and is_chars_and_digits and is_digits_valid:
        print("Password is valid")
    else:
        if not is_length_valid:
            print("Password must be between 6 and 10 characters")
        if not is_chars_and_digits:
            print("Password must consist only of letters and digits")
        if not is_digits_valid:
            print("Password must have at least 2 digits")


valid_password(password_as_string)


#02
# def password_validator(some_password: str) -> list:
#     list_of_errors = []
#     if len(some_password) < 6 or len(some_password) > 10:
#         list_of_errors.append("Password must be between 6 and 10 characters")
#     if not some_password.isalnum():
#         list_of_errors.append("Password must consist only of letters and digits")
#     digits_counter = 0
#     for character in some_password:
#         if character.isdigit():
#             digits_counter += 1
#     if digits_counter < 2:
#         list_of_errors.append("Password must have at least 2 digits")
#     return list_of_errors
#
#
# password = input()
# errors_in_password = password_validator(password)
# if errors_in_password == 0:
#     print("Password is valid")
# else:
#     print("\n".join(errors_in_password))
