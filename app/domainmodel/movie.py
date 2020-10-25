from app.domainmodel.genre import Genre
from app.domainmodel.actor import Actor
from app.domainmodel.director import Director


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
            self.__user_rating = ''
            self.__ratings = ''
            self.__metascore = ''
            self.__votes = ''
            self.__id: int

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def year(self):
        return self.__release_year

    @year.setter
    def year(self, year: int):
        self.__release_year = year

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

    @property
    def user_rating(self):
        return self.__user_rating

    @user_rating.setter
    def user_rating(self, rating):
        self.__user_rating = rating

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, score):
        self.__metascore = score

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, votes):
        self.__votes = votes

    @property
    def rating(self):
        return self.__ratings

    @rating.setter
    def rating(self, ratings):
        self.__ratings = ratings

    def __repr__(self):
        return f"<Movie {self.__movie_name}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__movie_name == other.__movie_name) and (self.__release_year == other.__release_year)

    def __lt__(self, other):
        if self.__movie_name != other.__movie_name:
            return self.__movie_name < other.__movie_name
        else:
            return self.__release_year < other.__release_year

    def __hash__(self):
        return hash((self.__movie_name, self.__release_year))

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    def add_director(self, director: Director):
        self.__director.append(director)

    def remove_director(self, director: Director):
        if director in self.__director:
            self.__actors.remove(director)