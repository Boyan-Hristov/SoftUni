from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Name", 1993, 9.6)

    def test_correct_init(self):
        self.assertEqual("Name", self.movie.name)
        self.assertEqual(1993, self.movie.year)
        self.assertEqual(9.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_failure_actor_already_added(self):
        self.movie.actors = ["Arnold"]
        result = self.movie.add_actor("Arnold")
        self.assertEqual("Arnold is already added in the list of actors!",
                         result)
        self.assertEqual(["Arnold"], self.movie.actors)

    def test_add_actor_success_actor_added(self):
        self.movie.add_actor("Arnold")
        self.assertEqual(["Arnold"], self.movie.actors)

    def test_greater_than_success(self):
        other = Movie("Movie", 2005, 8.6)
        self.assertEqual('"Name" is better than "Movie"', self.movie > other)

    def test_greater_than_failure(self):
        other = Movie("Movie", 2005, 9.8)
        self.assertEqual('"Movie" is better than "Name"', self.movie > other)

    def test_represent(self):
        self.movie.actors = ["Actor1", "Actor2", "Actor3"]
        expected = "Name: Name\n" \
                   "Year of Release: 1993\n" \
                   "Rating: 9.60\n" \
                   "Cast: Actor1, Actor2, Actor3"
        self.assertEqual(expected, str(self.movie))


if __name__ == "__main__":
    main()
