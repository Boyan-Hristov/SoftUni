integers = list(map(int, input().split()))
command = input()

while not command == "end":
    command_info = command.split()
    if "exchange" in command:
        if 0 <= int(command_info[1]) < len(integers):
            first_half = integers[:int(command_info[1]) + 1]
            second_half = integers[int(command_info[1]) + 1:]
            integers = second_half + first_half
        else:
            print("Invalid index")
    elif "max" in command:
        if "even" in command:
            max_even = 0
            for number in integers:
                if number % 2 == 0:
                    if number > max_even:
                        max_even = number
            if max_even == 0:
                output = "No matches"
            else:
                if integers.count(max_even) > 1:
                    output = len(integers) - integers[::-1].index(max_even) - 1
                else:
                    output = integers.index(max_even)
            print(output)
        elif "odd" in command:
            max_odd = 0
            for number in integers:
                if not number % 2 == 0:
                    if number > max_odd:
                        max_odd = number
            if max_odd == 0:
                output = "No matches"
            else:
                if integers.count(max_odd) > 1:
                    output = len(integers) - integers[::-1].index(max_odd) - 1
                else:
                    output = integers.index(max_odd)
            print(output)
    elif "min" in command:
        if "even" in command:
            min_even = 1001
            for number in integers:
                if number % 2 == 0:
                    if number < min_even:
                        min_even = number
            if min_even == 1001:
                output = "No matches"
            else:
                if integers.count(min_even) > 1:
                    output = len(integers) - integers[::-1].index(min_even) - 1
                else:
                    output = integers.index(min_even)
            print(output)
        elif "odd" in command:
            min_odd = 1001
            for number in integers:
                if not number % 2 == 0:
                    if number < min_odd:
                        min_odd = number
            if min_odd == 1001:
                output = "No matches"
            else:
                if integers.count(min_odd) > 1:
                    output = len(integers) - integers[::-1].index(min_odd) - 1
                else:
                    output = integers.index(min_odd)
            print(output)
    elif "first" in command:
        if int(command_info[1]) > len(integers):
            print("Invalid count")
        else:
            if "even" in command:
                even_numbers = []
                for number in integers:
                    if number % 2 == 0:
                        if len(even_numbers) == int(command_info[1]):
                            break
                        else:
                            even_numbers.append(number)
                print(even_numbers)
            elif "odd" in command:
                odd_numbers = []
                for number in integers:
                    if not number % 2 == 0:
                        if len(odd_numbers) == int(command_info[1]):
                            break
                        else:
                            odd_numbers.append(number)
                print(odd_numbers)
    elif "last" in command:
        if int(command_info[1]) > len(integers):
            print("Invalid count")
        else:
            reversed_integers = integers[::-1]
            if "even" in command:
                even_numbers = []
                for number in reversed_integers:
                    if number % 2 == 0:
                        if len(even_numbers) == int(command_info[1]):
                            break
                        else:
                            even_numbers.append(number)
                print(even_numbers)
            elif "odd" in command:
                odd_numbers = []
                for number in reversed_integers:
                    if not number % 2 == 0:
                        if len(odd_numbers) == int(command_info[1]):
                            break
                        else:
                            odd_numbers.append(number)
                print(odd_numbers)
    command = input()

print(integers)