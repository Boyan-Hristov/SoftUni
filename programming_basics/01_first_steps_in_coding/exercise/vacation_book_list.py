pages_amount = int(input())
pages_an_hour = int(input())
days_amount = int(input())

hours_required = pages_amount // pages_an_hour
hours_a_day = hours_required / days_amount

print(int(hours_a_day))
