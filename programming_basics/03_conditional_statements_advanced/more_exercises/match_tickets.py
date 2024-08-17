budget = float(input())
ticket_type = input()
people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

transport_percent_of_budget = 0
if 1 <= people <= 4:
    transport_percent_of_budget = 0.75
elif 5 <= people <= 9:
    transport_percent_of_budget = 0.6
elif 10 <= people <= 24:
    transport_percent_of_budget = 0.5
elif 25 <= people <= 49:
    transport_percent_of_budget = 0.4
else:
    transport_percent_of_budget = 0.25

transport_cost = budget * transport_percent_of_budget
money_for_tickets = budget - transport_cost

tickets_cost = 0
if ticket_type == "VIP":
    tickets_cost = people * vip_ticket
elif ticket_type == "Normal":
    tickets_cost = people * normal_ticket

total_expenses = transport_cost + tickets_cost

money_left = 0
money_needed = 0
if total_expenses <= budget:
    money_left = budget - total_expenses
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = total_expenses - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
