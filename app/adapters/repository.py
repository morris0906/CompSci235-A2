import abc
from typing import List
from datetime import date

from app.domainmodel.user import User
from app.domainmodel.movie import Movie
from app.domainmodel.actor import Actor
from app.domainmodel.genre import Genre
from app.domainmodel.review import Review
from app.domainmodel.director import Director

repository_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """" Adds a User to the repository. """
        raise NotImplementedError


    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id: int) -> Movie:
        """ Returns Movie with id from the repository.

        If there is no Movie with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, title: str) -> Movie:
        """ Returns Movie with given title.

        If there are no Movies with that title, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_for_genre(self, genre_name: str):
        """ Returns a list of ids representing Movies that are tagged by genre_name.

        If there are no Movies that are tagged by genre_name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_for_director(self, director_name: str):
        """ Returns a list of ids representing Movies that are tagged by director name.

        If there are no Movies that are tagged by director name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_for_actor(self, actor_name: str):
        """ Returns a list of ids representing Movies that are tagged by actor name.

        If there are no Movies that are tagged by actor name, this method returns an empty list.
        """
        raise NotImplementedError

    def get_reviews_for_movie(movie:Movie):
        """ Returns a list of ids representing Movies that are tagged by actor name.

                If there are no Movies that are tagged by actor name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """ Adds a Actor to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        """ Returns the Actors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError