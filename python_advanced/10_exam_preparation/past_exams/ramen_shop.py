from collections import deque

ramen = [int(x) for x in input().split(", ")]
customers = deque([int(y) for y in input().split(", ")])

while ramen and customers:
    bowl = ramen.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl -= customer
        ramen.append(bowl)

    elif bowl < customer:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")



