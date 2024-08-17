from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[object] = []

    def register_user(self, username: str, age: int):
        try:
            next(filter(lambda u: u.username == username, self.users_collection))
            raise Exception("User already exists!")
        except StopIteration:
            user = User(username, age)
            self.users_collection.append(user)
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception("This user does not exist!")

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # check sequence of logic
        user.movies_owned.append(movie)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        # movie_attributes = {
        #     "title": movie.title,
        #     "year": movie.year,
        #     "age_restriction": movie.age_restriction
        # }
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # check if logic works -> doesn't work
        # for attribute, new_value in kwargs.items():
        #     movie_attributes[attribute] = new_value

        for attribute, new_value in kwargs.items():
            if attribute == "title":
                movie.title = new_value
            elif attribute == "year":
                movie.year = new_value
            elif attribute == "age_restriction":
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        elif movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        else:
            movie.likes += 1
            user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        return "\n".join([m.details() for m in sorted(self.movies_collection, key=lambda m: (-m.year, m.title))])

    def __str__(self):
        result = f"All users: {', '.join(u.username for u in self.users_collection)}\n" \
            if self.users_collection else "All users: No users.\n"
        result += f"All movies: {', '.join(m.title for m in self.movies_collection)}" \
            if self.movies_collection else "All movies: No movies."

        return result
