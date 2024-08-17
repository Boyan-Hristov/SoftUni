from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Bruno", 60, 100, 2)

    def test_correct_init(self):
        self.assertEqual("Bruno", self.hero.username)
        self.assertEqual(60, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_battle_with_yourself(self):
        enemy_hero = Hero("Bruno", 50, 80, 1)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_health(self):
        self.hero.health = 0
        enemy_hero = Hero("Kosio", 50, 0, 1)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_without_enemy_health(self):
        enemy_hero = Hero("Kosio", 50, 0, 1)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Kosio. He needs to rest", str(ve.exception))

    def test_battle_draw(self):
        enemy_hero = Hero("Kosio", 50, 120, 2)
        self.assertEqual("Draw", self.hero.battle(enemy_hero))
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_battle_win_expected_both_heroes_health_decrease_self_health_level_damage_increase(self):
        enemy_hero = Hero("Kosio", 50, 100, 1)
        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(61, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(7, self.hero.damage)
        self.assertEqual(-20, enemy_hero.health)

    def test_battle_lose_expected_both_heroes_health_decrease_enemy_health_level_damage_increase(self):
        enemy_hero = Hero("Kosio", 70, 150, 2)
        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(71, enemy_hero.level)
        self.assertEqual(35, enemy_hero.health)
        self.assertEqual(7, enemy_hero.damage)
        self.assertEqual(-40, self.hero.health)

    def test_str(self):
        self.assertEqual("Hero Bruno: 60 lvl\n"
                         "Health: 100\n"
                         "Damage: 2\n", self.hero.__str__())


if __name__ == "__main__":
    main()
