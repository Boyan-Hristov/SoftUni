from collections import deque

substrings = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

colors_found = []
colors_on_hold = []
popped_elements = deque()

while substrings:
    if len(substrings) == 1:
        substring = substrings.pop()
        if substring in all_colors:
            if substring in main_colors:
                colors_found.append(substring)
            else:
                if secondary_colors[substring][0] in colors_found and secondary_colors[substring][1] in colors_found:
                    colors_found.append(substring)

    else:
        first_substring, last_substring = substrings.popleft(), substrings.pop()
        color = first_substring + last_substring
        if color in all_colors:
            if color in main_colors:
                colors_found.append(color)
            else:
                if secondary_colors[color][0] in colors_found and secondary_colors[color][1] in colors_found:
                    colors_found.append(color)
                else:
                    colors_on_hold.append(color)
        else:
            first_substring = first_substring[:len(first_substring) - 1]
            last_substring = last_substring[:len(last_substring) - 1]
            elements_to_pop = len(substrings) // 2
            for i in range(elements_to_pop):
                popped_elements.appendleft(substrings.popleft())
            if last_substring:
                substrings.appendleft(last_substring)
            if first_substring:
                substrings.appendleft(first_substring)
            for j in range(len(popped_elements)):
                substrings.appendleft(popped_elements.popleft())

for color_on_hold in colors_on_hold:
    if secondary_colors[color_on_hold][0] in colors_found and secondary_colors[color_on_hold][1] in colors_found:
        colors_found.append(color_on_hold)

print(colors_found)



