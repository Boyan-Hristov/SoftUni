import os

path = os.path.join("files", "text.txt")

with open(path, "r") as file:
    text = file.readlines()

characters = ("-", ",", ".", "!", "?")

for row in range(0, len(text), 2):
    for character in characters:
        text[row] = text[row].replace(character, "@")

    print(text[row].strip()[::-1])
