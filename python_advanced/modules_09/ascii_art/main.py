from pyfiglet import figlet_format


def print_art(message):
    ascii_art = figlet_format(message, "isometric3")
    print(ascii_art)


text = input()
print_art(text)
