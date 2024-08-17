page_cost = float(input())
cover_cost = float(input())
discount_percent = int(input())
designer_cost = float(input())
team_involvement_percent = int(input())

pages = 899
covers = 2

book_cost = page_cost * pages + cover_cost * covers

discount = discount_percent / 100
discount_cost = book_cost * (1 - discount)

book_cost_designer = discount_cost + designer_cost

team_involvement = team_involvement_percent / 100
final_book_cost = book_cost_designer * (1 - team_involvement)

print(f"Avtonom should pay {final_book_cost:.2f} BGN.")