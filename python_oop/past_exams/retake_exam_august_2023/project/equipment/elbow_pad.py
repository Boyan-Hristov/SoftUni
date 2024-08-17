from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    @property
    def price_increment(self):
        return 1.1
