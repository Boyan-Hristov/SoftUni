while True:
    double_string = ""
    command = input()
    if command == "End":
        break
    if command != "SoftUni":
        for letter in command:
            double_string += 2 * letter
        print(double_string)
