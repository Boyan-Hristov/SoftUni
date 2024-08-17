employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

improved_happiness = [happiness * improvement_factor for happiness in employees_happiness]
average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_employees = [employee for employee in improved_happiness if employee > average_happiness]
if len(happy_employees) >= len(improved_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are not happy!")


# 02
# employees_happiness = list(map(int, input().split()))
# improvement_factor = int(input())
#
# employees_happiness = list(map(lambda x: x * improvement_factor, employees_happiness))
# average_happiness = sum(employees_happiness) / len(employees_happiness)
# happy_employees = list(filter(lambda x: x >= average_happiness, employees_happiness))
# if len(happy_employees) >= len(employees_happiness) / 2:
#     print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")

