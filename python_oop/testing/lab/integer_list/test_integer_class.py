from unittest import TestCase, main
from integer_list.integer_class import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.a = IntegerList(4.5, 1, 2, 3, "Hello")

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.a.get_data())

    def test_add_method_with_invalid_argument_type(self):
        with self.assertRaises(ValueError) as ve:
            self.a.add(4.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_method_expected_element_added_to_list(self):
        self.a.add(4)
        self.assertEqual([1, 2, 3, 4], self.a.get_data())

    def test_remove_index_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.a.remove_index(10)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_method_expected_element_at_index_removed(self):
        r = self.a.get_data()[0]
        t = self.a.remove_index(0)
        self.assertEqual([2, 3], self.a.get_data())
        self.assertEqual(r, t)

    def test_get_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.a.get(10)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_expected_value_at_index(self):
        self.assertEqual(1, self.a.get_data()[0])

    def test_insert_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.a.insert(10, 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_with_invalid_element_type(self):
        with self.assertRaises(ValueError) as ve:
            self.a.insert(0, "abc")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_expected_element_added_to_list_at_given_index(self):
        self.a.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], self.a.get_data())

    def test_get_biggest_method_expected_biggest_number_in_list(self):
        self.assertEqual(3, self.a.get_biggest())

    def test_get_index_method_expected_index_at_which_is_element(self):
        self.assertEqual(0, self.a.get_index(1))


if __name__ == "__main__":
    main()
