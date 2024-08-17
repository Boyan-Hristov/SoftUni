locations = int(input())

for location in range(locations):
    expected_average_extraction = float(input())
    days = int(input())
    total_extracted_gold = 0
    for day in range(days):
        extracted_gold = float(input())
        total_extracted_gold += extracted_gold
    average_extraction = total_extracted_gold / days
    gold_needed = 0
    if average_extraction >= expected_average_extraction:
        print(f"Good job! Average gold per day: {average_extraction:.2f}.")
    else:
        gold_needed = expected_average_extraction - average_extraction
        print(f"You need {gold_needed:.2f} gold.")


