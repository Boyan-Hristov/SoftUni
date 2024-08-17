tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) == 20:
        if "@" in ticket or "#" in ticket or "$" or "^" in ticket:
            first_half = ticket[:10]
            second_half = ticket[10:]
            first_sequence = ""
            first_sequence_length = 0
            second_sequence = ""
            second_sequence_length = 0
            winning_symbol = ""
            for char in first_half:
                if char == "@" or char == "#" or char == "$" or char == "^":
                    winning_symbol = char
                    first_sequence += char
                    if len(first_sequence) > first_sequence_length:
                        first_sequence_length = len(first_sequence)
                else:
                    first_sequence = ""
            for char in second_half:
                if char == "@" or char == "#" or char == "$" or char == "^":
                    second_sequence += char
                    if len(second_sequence) > second_sequence_length:
                        second_sequence_length = len(second_sequence)
                else:
                    second_sequence = ""
            if first_sequence_length == 10 and second_sequence_length == 10:
                print(f'ticket "{ticket}" - {first_sequence_length}{winning_symbol} Jackpot!')
            elif first_sequence_length >= 6 and second_sequence_length >= 6:
                if first_sequence_length >= second_sequence_length:
                    winning_sequence_length = second_sequence_length
                else:
                    winning_sequence_length = first_sequence_length
                print(f'ticket "{ticket}" - {winning_sequence_length}{winning_symbol}')
            else:
                print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")


# def check_ticket(ticket):
#     if len(ticket) != 20:
#         return "invalid ticket"
#     winning_symbols = ['@', '#', '$', '^']
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#     for match_symbol in winning_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbol_repetition = match_symbol * uninterrupted_match_length
#             # We have winning ticket
#             if winning_symbol_repetition in left_part \
#                     and winning_symbol_repetition in right_part:
#                 if uninterrupted_match_length == 10:
#                     return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
#                 return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
#     return f'ticket "{ticket}" - no match'
#
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# for current_ticket in tickets:
#     print(check_ticket(current_ticket))
