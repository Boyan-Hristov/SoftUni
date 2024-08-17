from string import punctuation
import os

path = os.path.join("files", "text.txt")

with open(path, "r") as file:
    text = file.readlines()

for line in range(len(text)):
    letters = 0
    marks = 0

    for symbol in text[line]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_path = os.path.join("files", "output.txt")
    output_file = open(output_path, "a")
    output_file.write(f"Line {line + 1}: {text[line].strip()} ({letters})({marks})\n")
    output_file.close()
