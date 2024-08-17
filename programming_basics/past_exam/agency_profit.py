company_name = input()
regular_tickets = int(input())
children_tickets = int(input())
regulat_ticket_price = float(input())
service_tax = float(input())

children_ticket_price = regulat_ticket_price * 0.3
regular_tickets_revenue = regular_tickets * regulat_ticket_price + regular_tickets * service_tax
children_tickets_revenue = children_tickets * children_ticket_price + children_tickets * service_tax
total_revenue = children_tickets_revenue + regular_tickets_revenue
profit = total_revenue * 0.2
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")