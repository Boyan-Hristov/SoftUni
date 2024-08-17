from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Timon", "cat", "meow")

    def test_correct_init(self):
        self.assertEqual("Timon", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom())

    def test_make_sound(self):
        self.assertEqual("Timon makes meow", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Timon is of type cat", self.mammal.info())


if __name__ == "__main__":
    main()
