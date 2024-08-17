import re

numbers = []
text = input()
pattern = re.compile(r"\d+")
while text != "":
    matches = re.findall(pattern, text)
    for match in matches:
        numbers.append(match)
    text = input()

print(" ".join(numbers))
