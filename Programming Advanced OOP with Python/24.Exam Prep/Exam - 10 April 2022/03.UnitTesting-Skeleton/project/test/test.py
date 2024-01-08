from project.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("The Dragon", 2002, 10)

    def test_correct_init_movie(self):
        self.assertEqual(self.movie.name, "The Dragon")
        self.assertEqual(self.movie.year, 2002)
        self.assertEqual(self.movie.rating, 10)
        self.assertEqual(self.movie.actors, [])

    def test_name_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_before_1887_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_not_in_list(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("Bruce Lee")
        self.assertEqual(["Bruce Lee"], self.movie.actors)

    def test_actor_in_list_expect_message(self):
        self.movie.add_actor("Bruce Lee")
        result = self.movie.add_actor("Bruce Lee")

        self.assertEqual("Bruce Lee is already added in the list of actors!", result)

    def test_movie_rating_first_movie_greater_than_second(self):
        new_movie = Movie("Elvis", 2022, 9.5)

        result = self.movie > new_movie
        self.assertEqual('"The Dragon" is better than "Elvis"', result)

    def test_movie_rating_second_movie_greater_than_first(self):
        new_movie = Movie("Elvis", 2022, 9.5)

        result = new_movie > self.movie
        self.assertEqual('"The Dragon" is better than "Elvis"', result)

    def test_repr(self):
        self.movie.add_actor("Bruce Lee")
        self.movie.add_actor("Sylvester Stallone")
        expected = f"Name: The Dragon\n" \
                   "Year of Release: 2002\n" \
                   "Rating: 10.00\n" \
                   "Cast: Bruce Lee, Sylvester Stallone"

        result = self.movie.__repr__()
        self.assertEqual(expected, result)
