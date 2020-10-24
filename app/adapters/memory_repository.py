import os, csv
from datetime import datetime
from typing import List

from app.adapters.repository import AbstractRepository
from app.domainmodel.user import User
from app.domainmodel.movie import Movie
from app.domainmodel.actor import Actor
from app.domainmodel.genre import Genre
from app.domainmodel.director import Director



class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._users = list()
        self._movies = list()
        self._movies_index = dict()
        self._genres = list()
        self._actors = list()
        self._directors = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    def add_movie(self, movie: Movie):
        self._movies.append(movie)

    def get_movie(self, title: str, year: int) -> Movie:
        pass

    def get_number_of_movies(self):
        return len(self._movies)

    def get_movies_by_title(self, title: str) -> List[Movie]:
        movie_list = []
        for movie in self._movies:
            if title ==movie.title:
                movie_list.append(movie)
        return movie_list

    def get_movies_for_actor(self, actor_name: str):
        movie_list = []
        for movie in self._movies:
            if len(movie.actors) > 0:
                if Actor(actor_name) in movie.actors:
                    movie_list.append(movie)
        return movie_list

    def get_movies_for_director(self, director_name: str):
        movie_list = []
        for movie in self._movies:
            if len(movie.director) > 0:
                if Director(director_name) in movie.director:
                    movie_list.append(movie)
        return movie_list

    def get_movies_for_genre(self, genre_name: str):
        moive_list = []
        for movie in self._movies:
            if len(movie.genres) > 0:
                if Genre(genre_name) in movie.genres:
                    moive_list.append(movie)
        return moive_list

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

