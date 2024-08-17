import re

text = input()
while text != "":
    pattern = r"(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)"
    matches = re.search(pattern, text)
    if matches:
        print(matches.group(1))
    text = input()
