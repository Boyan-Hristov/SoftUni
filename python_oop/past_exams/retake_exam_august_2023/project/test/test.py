from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(50_000, 4, True)

    def test_correct_init(self):
        self.assertEqual(50_000, self.trip.budget)
        self.assertEqual(4, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual({'New Zealand': 7500,
                          'Australia': 5700,
                          'Brazil': 6200,
                          'Bulgaria': 500},
                         self.trip.DESTINATION_PRICES_PER_PERSON)

    def test_travelers_setter_with_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_with_one_traveler(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_is_family_setter_with_more_than_two_travelers(self):
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

    def test_book_a_trip_with_invalid_destination_expected_returns_message(self):
        result = self.trip.book_a_trip("Spain")
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         result)

    def test_book_a_trip_with_valid_destination_and_family_discount_not_enough_budget(self):
        self.trip.budget = 1700
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_with_valid_destination_no_family_discount_and_not_enough_budget(self):
        self.trip.budget = 1900
        self.trip.is_family = False
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_valid_destination_family_discount_enough_budget_expected_decrease_budget_and_fill_booked_destinations(self):
        destination = "New Zealand"
        result = self.trip.book_a_trip(destination)
        self.assertEqual({destination: 27_000}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(23_000, self.trip.budget)
        self.assertEqual(f'Successfully booked destination {destination}! '
                         f'Your budget left is {self.trip.budget:.2f}',
                         result)

    def test_book_a_trip_valid_destination_no_family_discount_enough_budget_expected_decrease_budget_and_fill_booked_destinations(self):
        self.trip.is_family = False
        destination = "Australia"
        result = self.trip.book_a_trip(destination)
        self.assertEqual({destination: 22_800}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(27_200, self.trip.budget)
        self.assertEqual(f'Successfully booked destination {destination}! '
                         f'Your budget left is {self.trip.budget:.2f}',
                         result)

    def test_booking_status_no_booked_destinations(self):
        result = self.trip.booking_status()
        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}',
                         result)
        self.assertEqual(50_000, self.trip.budget)

    def test_booking_status_expected_returns_info_about_booked_destinations(self):
        self.trip.is_family = False
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("Australia")
        result = self.trip.booking_status()
        self.assertEqual("Booked Destination: Australia\n"
                         "Paid Amount: 22800.00\n"
                         "Booked Destination: Bulgaria\n"
                         "Paid Amount: 2000.00\n"
                         "Number of Travelers: 4\n"
                         "Budget Left: 25200.00",
                         result)


if __name__ == "__main__":
    main()
