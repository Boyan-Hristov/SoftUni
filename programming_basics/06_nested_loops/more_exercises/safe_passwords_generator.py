a = int(input())
b = int(input())
max_passwords = int(input())

A = 35
B = 64
x = 1
y = 1

for password in range(max_passwords):
    print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
    A += 1
    B += 1
    y += 1
    if A > 55:
        A = 35
    if B > 96:
        B = 64
    if y > b:
        x += 1
        y = 1
    if x > a and y > b:
        break


