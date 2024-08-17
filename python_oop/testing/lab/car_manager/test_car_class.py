from unittest import TestCase, main
# from car_manager.car_class import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Skoda", "Octavia", 10, 60)

    def test_correct_init(self):
        self.assertEqual("Skoda", self.car.make)
        self.assertEqual("Octavia", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_without_input(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_without_input(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_without_input(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_without_input(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_without_input(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_without_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_expected_fuel_amount_increase_no_more_than_fuel_capacity(self):
        self.car.refuel(100)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_expected_decrease_fuel_amount(self):
        self.car.refuel(60)
        self.car.drive(10)
        self.assertEqual(59, self.car.fuel_amount)


if __name__ == "__main__":
    main()
