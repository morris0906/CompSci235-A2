from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, movie_name: str, release_year: int):
        if (movie_name == "" or type(movie_name) is not str) and release_year < 1900:
            self.__movie_name = None
            self.__release_year = None
        else:
            self.__movie_name = movie_name.strip()
            self.__release_year = release_year
            self.__actors = []
            self.__director: Director
            self.__description: str
            self.__runtime: int
            self.__genres = []

    @property
    def title(self) -> str:
        return self.__movie_name

    # this is a short description text of the movie. leading and trailing whitespace has to be removed
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description.strip()

    # here we need one of our Director objects, there is only one director associated with a movie
    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        self.__director = director

    # use a Python list to store one or more than one actors associated with this movie
    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors):
        self.__actors.append(actors) if type(actors) == Actor else self.__actors.extend(actors)

    # use a Python list to store one or more than one genres associated with this movie
    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres):
        self.__genres.append(genres) if type(genres) == Genre else self.__genres.extend(genres)

    # Constraint: the runtime is a positive number. A ValueError has to be raised if this constraint is not met.
    @property
    def runtime_minutes(self):
        return self.__runtime

    @runtime_minutes.setter
    def runtime_minutes(self, runtime: int):
        if runtime <= 0:
            raise ValueError
        else:
            self.__runtime = runtime

    def __repr__(self):
        return f"<Movie {self.__movie_name}, {self.__release_year}>"

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __hash__(self):
        pass

    def add_actor(self, actor: Actor):
        pass

    def remove_actor(self, actor: Actor):
        pass

    def add_genre(self, genre: Genre):
        pass

    def remove_genre(self, genre: Genre):
        pass