import app.domainmodel.movie as movies
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
            self.__director_movies = []

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @property
    def director_movies(self):
        return self.__director_movies

    def add_movie(self, movie: movies):
        self.__director_movies.append(movie)

    def is_related(self, movie: movies) -> bool:
        return movie in self.__director_movies

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        # TODO
        if not isinstance(other, Director):
            return False
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        # TODO
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        # TODO
        return hash(self.__director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None
