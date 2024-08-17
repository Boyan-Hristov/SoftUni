import re

text = input()
pattern = r"([\:\*]){2}([A-Z][a-z]{2,})(\1){2}"
digit_pattern = r"\d"
emoji_matches = re.findall(pattern, text)
digit_matches = re.findall(digit_pattern, text)
digit_matches = [int(digit) for digit in digit_matches]

cool_threshold = 1
for number in digit_matches:
    cool_threshold *= number

cool_emojis = []
for match in emoji_matches:
    emoji = match[1]
    emoji_coolness = 0
    for letter in emoji:
        emoji_coolness += ord(letter)
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(match[0] * 2 + emoji + match[2] * 2)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_matches)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojis:
    print(cool_emoji)
