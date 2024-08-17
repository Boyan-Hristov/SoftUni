type_of_data = input()
data_value = input()


def data_type(data):
    if type_of_data == "int":
        data = int(data_value)
        result = data * 2
    elif type_of_data == "real":
        data = float(data_value)
        result = f"{(data * 1.5):.2f}"
    elif type_of_data == "string":
        result = f"${data_value}$"
    return result


print(data_type(data_value))