rows = 2
cols = 11

album = [[f"{'-' * cols}"]]

for i in range(rows):
    row = [" " * cols]
    row.extend("\n")
    row.extend(f"{'-' * cols}")
    album.append(row)

[print(*row) for row in album]
