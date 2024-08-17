from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("Octavia", "Sedan", 200_000, 6_500)

    def test_correct_init(self):
        self.assertEqual("Octavia", self.car.model)
        self.assertEqual("Sedan", self.car.car_type)
        self.assertEqual(200_000, self.car.mileage)
        self.assertEqual(6_500, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_invalid_price_expected_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.9
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_invalid_mileage_expected_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 90
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ve.exception))

    def test_set_promotional_price_invalid_price_expected_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(7_000)
        self.assertEqual('You are supposed to decrease the price!',
                         str(ve.exception))

    def test_set_promotional_price_success_expected_price_decreased(self):
        result = self.car.set_promotional_price(5_000)
        self.assertEqual(5_000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.',
                         result)

    def test_need_repair_price_too_high(self):
        result = self.car.need_repair(3_500, "engine segments")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_success_expected_price_increase_repair_added(self):
        result = self.car.need_repair(2_000, "new transmission")
        self.assertEqual(8_500, self.car.price)
        self.assertEqual(["new transmission"], self.car.repairs)
        self.assertEqual(f'Price has been increased due to repair charges.',
                         result)

    def test_gt_not_matching_car_types(self):
        new_car = SecondHandCar("XC 90", "SUV", 150_000, 10_000)
        result = self.car > new_car
        self.assertEqual('Cars cannot be compared. Type mismatch!',
                         result)

    def test_gt_success_expected_bool_value(self):
        new_car = SecondHandCar("Superb", "Sedan", 150_000, 10_000)
        result = self.car > new_car
        self.assertFalse(result)

    def test_str_expected_car_info_as_string(self):
        self.car.need_repair(2_000, "new transmission")
        result = str(self.car)
        self.assertEqual("""Model Octavia | Type Sedan | Milage 200000km
Current price: 8500.00 | Number of Repairs: 1""", result)


if __name__ == "__main__":
    main()
