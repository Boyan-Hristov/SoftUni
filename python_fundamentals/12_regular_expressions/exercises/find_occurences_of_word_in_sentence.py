import re

text = input()
searched_word = input()
pattern = fr"{searched_word}\b"
matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))
