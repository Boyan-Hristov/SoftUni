number_of_lines = int(input())
unique_elements = set()

for i in range(number_of_lines):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

print("\n".join(unique_elements))
