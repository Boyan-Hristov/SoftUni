from math import log
from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    VALID_PROCESSORS= {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    MAX_RAM: int = 128

    def validate_processor(self, processor_type: str) -> bool:
        if processor_type not in self.VALID_PROCESSORS:
            return False
        return True

    def validate_ram(self, ram_value: int) -> bool:
        if not log(ram_value, 2).is_integer() or log(ram_value, 2) > self.MAX_RAM:
            return False
        return True

    def set_price(self, processor: str, ram_value: int) -> None:
        ram_price = log(ram_value, 2) * 100
        processor_price = self.VALID_PROCESSORS[processor]
        self.price = ram_price + processor_price

    def configure_computer(self, processor: str, ram: int) -> str:
        if not self.validate_processor(processor):
            raise ValueError(f"{processor} is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")

        if not self.validate_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.set_price(processor, ram)

        return f"Created {self.manufacturer} {self.model} with " \
               f"{self.processor} and {self.ram}GB RAM for {int(self.price)}$."
