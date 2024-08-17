target = int(input())
command = input()

cash_collected = 0
credit_collected = 0
payment_counter = 0
cash_payments = 0
credit_card_payments = 0
is_target_reached = False

while not command == "End":
    payment_counter += 1
    if payment_counter % 2 == 0:
        if float(command) < 10:
            print("Error in transaction!")
        else:
            credit_collected += float(command)
            credit_card_payments += 1
            print("Product sold!")
    else:
        if float(command) > 100:
            print("Error in transaction!")
        else:
            cash_collected += float(command)
            cash_payments += 1
            print("Product sold!")
    if cash_collected + credit_collected >= target:
        is_target_reached = True
        break

    command = input()

if is_target_reached == True:
    average_cash_transaction = cash_collected / cash_payments
    print(f"Average CS: {average_cash_transaction:.2f}")
    average_credit_card_transaction = credit_collected / credit_card_payments
    print(f"Average CC: {average_credit_card_transaction:.2f}")
if is_target_reached == False:
    print("Failed to collect required money for charity.")