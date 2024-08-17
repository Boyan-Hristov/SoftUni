men = int(input())
women = int(input())
tables = int(input())

tables_taken = 0

for man in range(1, men + 1):
    if tables_taken > tables:
        break
    else:
        for woman in range(1, women + 1):
            tables_taken += 1
            if tables_taken > tables:
                break
            else:
                print(f"({man} <-> {woman})", end=" ")
