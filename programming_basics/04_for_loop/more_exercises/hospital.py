days = int(input())

current_day = 0
patients_examined = 0
patients_not_examined = 0
doctors = 7

for day in range(days):
    patients = int(input())
    current_day += 1
    if current_day % 3 == 0:
        if patients_not_examined > patients_examined:
            doctors += 1
    if patients <= doctors:
        patients_examined += patients
    else:
        patients_treated = doctors
        patients_examined += patients_treated
        patients_untreated = patients - doctors
        patients_not_examined += patients_untreated

print(f"Treated patients: {patients_examined}.")
print(f"Untreated patients: {patients_not_examined}.")


