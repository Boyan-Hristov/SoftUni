from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTERS = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS.keys():
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        try:
            computer = next(filter(lambda c: c.price <= client_budget and
                                   c.processor == wanted_processor and
                                   c.ram >= wanted_ram, self.warehouse))
        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."


