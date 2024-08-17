# import re
#
# mirror_words = []
# string = input()
# pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
# matches = re.findall(pattern, string)
# if not matches:
#     print("No word pairs found!")
# else:
#     print(f"{len(matches)} word pairs found!")
#     for match in matches:
#         if match[1] == match[2][::-1]:
#             mirror_word = f"{match[1]} <=> {match[2]}"
#             mirror_words.append(mirror_word)
# if not mirror_words:
#     print("No mirror words!")
# else:
#     print(f"The mirror words are:")
#     print(", ".join(mirror_words))

import re

mirror_words = []
text = input()
pattern = r"([\@\#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
matches = re.findall(pattern, text)
for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(match[1] + " <=> " + match[2])
if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
