from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}
colors_found = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""

    for result in (first_word + second_word, second_word + first_word):
        if result in colors:
            colors_found.append(result)
            break
    else:
        for element in (first_word[:-1], second_word[:-1]):
            if element:
                words.insert(len(words) // 2, element)

for color in set(secondary_colors.keys()).intersection(colors_found):
    if not secondary_colors[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)
