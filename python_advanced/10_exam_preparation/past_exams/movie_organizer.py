def movie_organizer(*args) -> str:
    result = ""
    movies = {}

    for data in args:
        movie, genre = data
        if genre not in movies.keys():
            movies[genre] = []
        movies[genre].append(movie)

    for key, value in movies.items():
        movies[key] = sorted(value)

    movies = dict(sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, value in movies.items():
        result += f"{key} - {len(value)}\n"
        for film in value:
            result += f"* {film}\n"

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))


