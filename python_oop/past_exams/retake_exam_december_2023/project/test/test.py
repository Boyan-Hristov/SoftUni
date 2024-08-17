from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self) -> None:
        self.robot = ClimbingRobot("Mountain", "part type", 5, 20)
        self.robot_with_software = ClimbingRobot("Indoor", "metal", 10, 1024)
        self.robot_with_software.install_software(
            {"name": "math",
             "capacity_consumption": 2,
             "memory_consumption": 24}
        )

    def test_correct_init_and_class_attribute_with_valid_category(self):
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'],
                         self.robot.ALLOWED_CATEGORIES)
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("part type", self.robot.part_type)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(20, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter_with_invalid_category_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "invalid"
        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}",
                         str(ve.exception))

    def test_get_used_capacity_returns_sum_of_software_capacity_consumption(self):
        self.assertEqual(2, self.robot_with_software.get_used_capacity())

    def test_get_available_capacity_returns_correct_integer(self):
        self.assertEqual(8, self.robot_with_software.get_available_capacity())

    def test_get_used_memory_returns_sum_of_software_memory_consumption(self):
        self.assertEqual(24, self.robot_with_software.get_used_memory())

    def test_available_memory_returns_correct_integer(self):
        self.assertEqual(1000, self.robot_with_software.get_available_memory())

    def test_install_software_with_enough_capacity_and_memory_available(self):
        result = self.robot.install_software({"name": "software",
                                              "capacity_consumption": 2,
                                              "memory_consumption": 5})
        expected_result = "Software 'software' successfully installed on Mountain part."
        self.assertEqual(expected_result, result)
        self.assertEqual([{"name": "software",
                           "capacity_consumption": 2,
                           "memory_consumption": 5}],
                         self.robot.installed_software)

    def test_install_software_without_enough_capacity_expected_failure(self):
        result = self.robot.install_software({"name": "software",
                                              "capacity_consumption": 10,
                                              "memory_consumption": 10})
        expected_result = "Software 'software' cannot be installed on Mountain part."
        self.assertEqual(expected_result, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_without_enough_memory_expected_failure(self):
        result = self.robot.install_software({"name": "software",
                                              "capacity_consumption": 3,
                                              "memory_consumption": 30})
        expected_result = "Software 'software' cannot be installed on Mountain part."
        self.assertEqual(expected_result, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_equal_capacity_and_memory_expected_success(self):
        result = self.robot.install_software({"name": "software",
                                              "capacity_consumption": 5,
                                              "memory_consumption": 20})
        expected_result = "Software 'software' successfully installed on Mountain part."
        self.assertEqual(expected_result, result)
        self.assertEqual([{"name": "software",
                           "capacity_consumption": 5,
                           "memory_consumption": 20}],
                         self.robot.installed_software)


if __name__ == "__main__":
    main()
