import app.domainmodel.movie as movies

from typing import List

class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()
            self.__genre_movies: List[movies] = list()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @property
    def genre_movies(self):
        return self.__genre_movies

    def add_movie(self, movie: movies):
        self.__genre_movies.append(movie)

    def is_related(self, movie: movies) -> bool:
        return movie in self.__genre_movies

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Comedy")
        assert repr(genre1) == "<Genre Comedy>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(42)
        assert genre3.genre_name is None
        genre4 = Genre("Comedy")
        genre5 = Genre("Horror")
        lst = [genre4, genre5]
        assert lst[0].genre_name == "Comedy"
