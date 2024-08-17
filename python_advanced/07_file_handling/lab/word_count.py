import os
import re

words_path = os.path.join("..", "resources", "words.txt")
input_path = os.path.join("..", "resources", "input.txt")
output_path = os.path.join("..", "resources", "output.txt")

with open(words_path, "r+") as words_file:
    searched_words_as_text = words_file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]

with open(input_path, "r+") as input_file:
    content = input_file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = rf"\b{searched_word}\b"
    results = re.findall(pattern, content)
    words_count[searched_word] = len(results)

sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, "a") as output_file:
    for word, count in sorted_words_count:
        output_file.write(f"{word} - {count}\n")
