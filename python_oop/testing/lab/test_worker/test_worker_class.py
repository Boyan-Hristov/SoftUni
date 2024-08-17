from unittest import TestCase, main
# from test_worker.class_test_worker import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Test", 2000, 100)

    def test_correct_init_with_name_salary_and_energy(self):
        expected_name = "Test"
        expected_salary = 2000
        expected_energy = 100
        expected_money = 0

        self.assertEqual(expected_name, self.worker.name)
        self.assertEqual(expected_salary, self.worker.salary)
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_method_without_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_method_with_energy_expected_increase_money_reduce_energy(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        for _ in range(2):
            self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_method_expected_increase_energy(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_method_expected_string_representation_including_name_and_money(self):
        expected_result = 'Test has saved 2000 money.'
        self.worker.work()

        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == "__main__":
    main()
