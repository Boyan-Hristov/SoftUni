from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS.keys():
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if client.__class__.__name__ == "Student":
            if not loan_type == "StudentLoan":
                raise Exception("Inappropriate loan type!")
        elif client.__class__.__name__ == "Adult":
            if not loan_type == "MortgageLoan":
                raise Exception("Inappropriate loan type!")

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                client.loans.append(loan)
                self.loans.remove(loan)
                break

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_count = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                loans_count += 1

        return f"Successfully changed {loans_count} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                clients_count += 1

        return f"Number of clients affected: {clients_count}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_income = sum([c.income for c in self.clients])
        granted_loans = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([sum([loan.amount for loan in c.loans]) for c in self.clients])
        available_loans = len(self.loans)
        available_sum = sum([loan.amount for loan in self.loans])
        average_client_interest_rate = sum([c.interest for c in self.clients]) / len(
            self.clients) if self.clients else 0

        return f"Active Clients: {active_clients}\n" \
               f"Total Income: {total_income:.2f}\n" \
               f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {available_loans}, Total Sum: {available_sum:.2f}\n" \
               f"Average Client Interest Rate: {average_client_interest_rate:.2f}"

