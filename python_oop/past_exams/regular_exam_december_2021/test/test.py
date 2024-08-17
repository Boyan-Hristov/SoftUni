from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team("Barcelona")

    def test_correct_init(self):
        self.assertEqual("Barcelona", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "CSKA 1948"
        self.assertEqual("Team Name can contain only letters!",
                         str(ve.exception))

    def test_add_member(self):
        self.team.members = {"Messi": 25, "Xavi": 28}
        result = self.team.add_member(Messi=25, Xavi=28, Iniesta=27, Neymar=23)
        self.assertEqual({"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23},
                         self.team.members)
        self.assertEqual("Successfully added: Iniesta, Neymar", result)

    def test_remove_member_failure_member_non_existent(self):
        result = self.team.remove_member("Messi")
        self.assertEqual("Member with name Messi does not exist", result)

    def test_remove_member_success_member_removed(self):
        self.team.members = {"Messi": 25, "Xavi": 28}
        result = self.team.remove_member("Messi")
        self.assertEqual({"Xavi": 28}, self.team.members)
        self.assertEqual("Member Messi removed", result)

    def test_greater_than_one_way(self):
        self.team.members = {"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23}
        other = Team("RealMadrid")
        other.members = {"Ronaldo": 27, "Benzema": 26}
        self.assertTrue(self.team > other)

    def test_greater_than_other_way(self):
        self.team.members = {"Ronaldo": 27, "Benzema": 26}
        other = Team("RealMadrid")
        other.members = {"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23}
        self.assertFalse(self.team > other)

    def test_len(self):
        self.team.members = {"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23}
        self.assertEqual(4, len(self.team))

    def test_add_creates_new_object(self):
        other = Team("Junior")
        self.team.members = {"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23}
        other.members = {"Ansu Fati": 15, "Lamine Yamal": 14, "Pedri": 15, "Gavi": 14}
        new_team = self.team.__add__(other)
        self.assertEqual("BarcelonaJunior", new_team.name)
        self.assertEqual({"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23,
                         "Ansu Fati": 15, "Lamine Yamal": 14, "Pedri": 15, "Gavi": 14},
                         new_team.members)

    def test_str(self):
        self.team.members = {"Messi": 25, "Xavi": 28, "Iniesta": 27, "Neymar": 23}
        expected = "Team name: Barcelona\n" \
                   "Member: Xavi - 28-years old\n" \
                   "Member: Iniesta - 27-years old\n" \
                   "Member: Messi - 25-years old\n" \
                   "Member: Neymar - 23-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == "__main__":
    main()
