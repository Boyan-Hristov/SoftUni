number_of_lines = int(input())

intersections = []

for i in range(number_of_lines):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_set = set()
    second_set = set()

    for number in range(int(first_start), int(first_end) + 1):
        first_set.add(number)

    for num in range(int(second_start), int(second_end) + 1):
        second_set.add(num)

    intersections.append(list(first_set.intersection(second_set)))

intersections.sort(key=len, reverse=True)

print(f"Longest intersection is {intersections[0]} with length {len(intersections[0])}")
