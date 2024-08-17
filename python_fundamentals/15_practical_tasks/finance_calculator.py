def main_menu():
    while True:
        action = input("Please select an operation:\n"
                       "1 - Calculate Simple Interest\n"
                       "2 - Calculate Compound Interest\n"
                       "3 - Calculate Loan Payment\n"
                       "4 - Calculate Future Value of Savings\n"
                       "5 - Quit\n")
        if action == "1" or action == "2" or action == "3" \
                or action == "4" or action == "5":
            return action
        else:
            print(f"Invalid operation. Please try again.")


def simple_interest(principal: float, interest_rate: float, years: float) -> float:
    interest = interest_rate / 100
    final_amount = principal * (1 + interest * years)
    final_interest = final_amount - principal
    return final_interest


def compound_interest(principal: float, interest_rate: float, years: float) -> float:
    interest = interest_rate / 100
    final_amount = principal * (1 + interest / 12) ** (12 * years)
    final_interest = final_amount - principal
    return final_interest


def loan_payment(principal: float, interest_rate: float, years: float) -> float:
    annual_interest = interest_rate / 100
    periodic_interest = annual_interest / 12
    total_payments = years * 12
    monthly_payment = principal * (periodic_interest * (1 + periodic_interest) ** total_payments) / \
        ((1 + periodic_interest) ** total_payments - 1)
    return monthly_payment


def savings(investment: float, interest_rate: float, years: float) -> float:
    interest = interest_rate / 100
    future_value = investment * (1 + interest) ** years
    return future_value


def terminate():
    print("Program terminated.")
    exit()


def choose():
    while True:
        choice = input("Do you want to perform another calculation? [Y]es / [N]o\n")
        if choice.lower() == "y":
            action = main_menu()
            return action
        elif choice.lower() == "n":
            terminate()
        else:
            print("Invalid input. Please try again.")


def number_validator(text: str) -> bool:
    try:
        float(text)
    except ValueError:
        return False
    else:
        return True


operation = main_menu()
while True:
    operation_info = {"principal": input("Enter principal amount: "),
                      "interest_rate": input("Enter interest rate percent: "),
                      "period": input("Enter duration (in years): ")}
    is_input_valid = True
    for value in operation_info.values():
        is_value_valid = number_validator(value)
        if not is_value_valid:
            is_input_valid = False
            break
    if not is_input_valid:
        print("Invalid input. Please try again.")
    else:
        principal_amount, interest_percent, duration = \
            float(operation_info["principal"]), \
            float(operation_info["interest_rate"]), \
            float(operation_info["period"])
        if operation == "1":
            total_simple_interest = simple_interest(principal_amount, interest_percent, duration)
            print(f"Simple interest: {total_simple_interest:.2f} $")
        elif operation == "2":
            total_compound_interest = compound_interest(principal_amount, interest_percent, duration)
            print(f"Compound interest: {total_compound_interest:.2f} $")
        elif operation == "3":
            total_monthly_payment = loan_payment(principal_amount, interest_percent, duration)
            print(f"Monthly payment: {total_monthly_payment:.2f} $")
        elif operation == "4":
            total_savings = savings(principal_amount, interest_percent, duration)
            print(f"Future value of savings: {total_savings:.2f} $")
        elif operation == "5":
            terminate()
    operation = choose()
