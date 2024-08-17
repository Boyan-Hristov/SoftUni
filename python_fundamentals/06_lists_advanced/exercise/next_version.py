software_version = list(map(int, input().split(".")))
#
software_version[-1] += 1
if software_version[-1] > 9:
    software_version[-1] = 0
    software_version[1] += 1
    if software_version[1] > 9:
        software_version[1] = 0
        software_version[0] += 1
software_version = list(map(str, software_version))
print(".".join(software_version))


# 02
# version = [int(digit) for digit in input().split(".")]
# version[-1] += 1
# for index in range(len(version) - 1, 0, -1):
#     if version[index] > 9:
#         version[index] = 0
#         version[index - 1] += 1
# print(".".join(str(number) for number in version))
