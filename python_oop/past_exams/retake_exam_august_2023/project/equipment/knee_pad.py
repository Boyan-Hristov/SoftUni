from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    @property
    def price_increment(self):
        return 1.2
