my_string = input()
letters_count = {}
for character in my_string:
    if character != " ":
        if character not in letters_count: # if we don't type .keys it automatically searches trough the keys by default
            letters_count[character] = 0
        letters_count[character] += 1
for letter, count in letters_count.items():
    print(f"{letter} -> {count}")
