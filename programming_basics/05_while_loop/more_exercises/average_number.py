#1
number = int(input())

counter = 0
sum = 0

while counter < number:
    current_number = int(input())
    counter += 1
    sum += current_number

average = sum / number
print(f"{average:.2f}")

#2
number = int(input())

sum = 0

for i in range(number):
    current_number = int(input())
    sum += current_number

average = sum / number
print(f"{average:.2f}")