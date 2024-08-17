import sys

n = int(input())

counter = 0
first_number = 0
pair = 0
maxdiff = -sys.maxsize

for number in range(n * 2):
    current_number = int(input())
    counter += 1
    if not counter % 2 == 0:
        first_number = current_number
    else:
        if counter >= 4:
            if abs(pair - (first_number + current_number)) > maxdiff:
                maxdiff = abs(pair - (first_number + current_number))
        pair = first_number + current_number

if counter == 2:
    print(f"Yes, value={pair}")
else:
    if maxdiff == 0:
        print(f"Yes, value={pair}")
    else:
        print(f"No, maxdiff={maxdiff}")





