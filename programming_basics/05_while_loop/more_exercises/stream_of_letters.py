symbol = input()

c_count = 0
o_count = 0
n_count = 0

message = ""

while not symbol == "End":
    if symbol.isalpha():
        if not symbol == "c" and not symbol == "o" and not symbol == "n":
            message += symbol
        elif symbol == "c":
            c_count += 1
            if c_count > 1:
                message += symbol
        elif symbol == "o":
            o_count += 1
            if o_count > 1:
                message += symbol
        elif symbol == "n":
            n_count += 1
            if n_count > 1:
                message += symbol
    if c_count > 0 and o_count > 0 and n_count > 0:
        print(message + " ", end = "")
        message = ""
        c_count = 0
        o_count = 0
        n_count = 0
    symbol = input()