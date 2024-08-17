from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: (Cheetah, Lion, Tiger), price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: (Caretaker, Keeper, Vet)):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        money_needed = sum([worker.salary for worker in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([animal.money_for_care for animal in self.animals])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {
            "Lion": [],
            "Tiger": [],
            "Cheetah": [],
        }
        status = [f"You have {len(self.animals)} animals"]

        for animal in self.animals:
            animals[f"{animal.__class__.__name__}"].append(f"{animal}")

        for key, value in animals.items():
            if value:
                status.append(f"----- {len(value)} {key}s:")
                status.extend(value)

        return "\n".join(status)

    def workers_status(self):
        workers = {
            "Keeper": [],
            "Caretaker": [],
            "Vet": [],
        }
        status = [f"You have {len(self.workers)} workers"]

        for worker in self.workers:
            workers[f"{worker.__class__.__name__}"].append(f"{worker}")

        for key, value in workers.items():
            if value:
                status.append(f"----- {len(value)} {key}s:")
                status.extend(value)

        return "\n".join(status)


