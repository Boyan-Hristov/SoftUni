from math import floor, sqrt

x_1_position = floor(float(input()))
y_1_position = floor(float(input()))
x_2_position = floor(float(input()))
y_2_position = floor(float(input()))


def closest_point(x_1, y_1, x_2, y_2):
    first_point_distance = floor(sqrt(x_1 ** 2 + y_1 ** 2))
    second_point_distance = floor(sqrt(x_2 ** 2 + y_2 ** 2))
    min_distance = ""
    if first_point_distance <= second_point_distance:
        min_distance = f"({x_1}, {y_1})"
    else:
        min_distance = f"({x_2}, {y_2})"
    return min_distance


print(closest_point(x_1_position, y_1_position, x_2_position, y_2_position))