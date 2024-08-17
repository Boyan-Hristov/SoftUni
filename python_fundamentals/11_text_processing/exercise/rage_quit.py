sequence = input()
symbols_used = ""
new_sequence = ""
subsequence = ""
for i in range(len(sequence)):
    if not sequence[i].isdigit():
        subsequence += sequence[i]
        if sequence[i].upper() not in symbols_used:
            symbols_used += sequence[i].upper()
    else:
        repeat_count = ""
        repeat_count += sequence[i]
        if i + 1 in range(len(sequence)):
            if sequence[i + 1].isdigit():
                repeat_count += sequence[i + 1]
        new_sequence += subsequence.upper() * int(repeat_count)
        subsequence = ""

print(f"Unique symbols used: {len(symbols_used)}")
print(new_sequence)
