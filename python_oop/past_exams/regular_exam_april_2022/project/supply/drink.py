from project.supply.supply import Supply


class Drink(Supply):

    def __init__(self, name: str, energy: int = 15):
        super().__init__(name, energy)
