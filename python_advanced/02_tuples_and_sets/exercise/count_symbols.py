text = input()
unique_characters = set(text)
sorted_characters = sorted(unique_characters)

for character in sorted_characters:
    print(f"{character}: {text.count(character)} time/s")
