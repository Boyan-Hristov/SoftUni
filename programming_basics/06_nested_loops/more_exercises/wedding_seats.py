last_sector = input()
rows_count = int(input())
odd_row_seats = int(input())

sector_loop_end = ord(last_sector)
rows_added = rows_count
seats_loop_end = ord("a") + odd_row_seats
total_seats = 0

for sector in range(65, sector_loop_end + 1):
    if sector == 65:
        rows_added += 1
        for row in range(1, rows_count + 1):
            if not row % 2 == 0:
                for seat in range(97, seats_loop_end):
                    print(f"{chr(sector)}{row}{chr(seat)}")
                    total_seats += 1
            else:
                for seat in range(97, seats_loop_end + 2):
                    print(f"{chr(sector)}{row}{chr(seat)}")
                    total_seats += 1

    else:
        rows_added += 1
        for row in range(1, rows_added):
            if not row % 2 == 0:
                for seat in range(97, seats_loop_end):
                    print(f"{chr(sector)}{row}{chr(seat)}")
                    total_seats += 1
            else:
                for seat in range(97, seats_loop_end + 2):
                    print(f"{chr(sector)}{row}{chr(seat)}")
                    total_seats += 1
print(total_seats)
