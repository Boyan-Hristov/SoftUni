from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

rotations = 0
matches = []


while len(matches) < 3:
    rotations += 1
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    character = chr(first_number + second_number)

    for number in (first_number, second_number):
        seat = str(number) + character
        if seat in seats:
            if seat not in matches:
                matches.append(seat)
                break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

    if rotations == 10:
        break

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")
