vowels = ["a", "o", "u", "e", "i"]


def no_vowels(string: str) -> str:
    vowelless_string = "".join([letter for letter in string if letter.lower() not in vowels])
    return vowelless_string


my_string = input()
print(no_vowels(my_string))
