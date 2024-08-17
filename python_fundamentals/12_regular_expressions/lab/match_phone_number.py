# import re
#
# phone_numbers = input()
# regex = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
# matches = re.findall(regex, phone_numbers)
# print(", ".join(matches))


import re

phone_numbers = input()
regex = r"\+359(\s|-)2\1\d{3}\1\d{4}\b"
matches = re.finditer(regex, phone_numbers)
for match in matches:
    print(match.group(), end=", ")
