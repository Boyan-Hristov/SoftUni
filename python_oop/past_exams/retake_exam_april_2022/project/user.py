from typing import List
from project.movie_specification.movie import Movie


class User:
    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}",
                  "Liked movies:"]
        result.extend([m.details() for m in self.movies_liked]) \
            if self.movies_liked else result.append("No movies liked.")
        result.append("Owned movies:")
        result.extend([m.details() for m in self.movies_owned]) \
            if self.movies_owned else result.append("No movies owned.")

        return "\n".join(result)
