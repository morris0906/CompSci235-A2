import csv
import os
from bisect import insort_left
from typing import List

from app.adapters.repository import AbstractRepository
from app.domainmodel.actor import Actor
from app.domainmodel.director import Director
from app.domainmodel.genre import Genre
from app.domainmodel.movie import Movie
from app.domainmodel.user import User


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
        insort_left(self._movies, movie)
        self._movies_index[movie.id] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None
        try:
            movie = self._movies_index[id]
        except KeyError:
            pass  # Ignore exception and return None.
        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    # def get_movies_by_title(self, title: str) -> List[Movie]:
    #     movie_list = []
    #     for movie in self._movies:
    #         if title == movie.title:
    #             movie_list.append(movie)
    #     return movie_list

    def get_movies_for_actor(self, actor_name: str):
        movie_list = []
        for movie in self._movies:
            if len(movie.actors) > 0:
                if Actor(actor_name) in movie.actors:
                    movie_list.append(movie.id)
        return movie_list

    def get_movies_for_director(self, director_name: str):
        movie_list = []
        for movie in self._movies:
            if len(movie.director) > 0:
                if Director(director_name) in movie.director:
                    movie_list.append(movie.id)
        return movie_list

    def get_movies_by_id(self, id_list):

        existing_ids = [id for id in id_list if id in self._movies_index]

        # Fetch the movies.
        movies = [self._movies_index[id] for id in existing_ids]
        return movies

    def get_movies_id_all(self):
        movie_ids = [movie.id for movie in self._movies]
        return movie_ids

    def get_movies_for_genre(self, genre_name: str):
        movie_list = []
        for movie in self._movies:
            if len(movie.genres) > 0:
                if Genre(genre_name) in movie.genres:
                    movie_list.append(movie.id)
        return movie_list

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


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    def read_csv(filename):
        with open(filename, encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.reader(csvfile)

            for row in movie_file_reader:
                row = [obj.strip() for obj in row]
                yield row

    for row in read_csv(os.path.join(data_path)):
        user = User(user_name=row[1], password=row[2])
        repo.add_user(user)
        users[row[0]] = user

    return users


def load_movies(data_path: str, repo: MemoryRepository):
    genres = dict()
    actors = dict()
    directors = dict()

    def read_csv(filename):
        with open(filename, encoding='utf-8-sig') as csvfile:
            file_reader = csv.reader(csvfile)

            for movie_row in file_reader:
                movie_row = [obj.strip() for obj in movie_row]
                yield movie_row

    for row in read_csv(os.path.join(data_path)):

        movie_id = row[0]
        movie_genres = row[2].split(',')
        movie_actors = row[5].split(',')
        movie_director = row[4].strip()

        # Add genres
        for genre in movie_genres:
            genre = genre.strip()
            if genre not in genres.keys():
                genres[genre] = list()
            genres[genre].append(movie_id)

        # Add actors
        for actor in movie_actors:
            actor = actor.strip()
            if actor not in actors.keys():
                actors[actor] = list()
            actors[actor].append(movie_id)

        # Add directors
        if movie_director not in directors.keys():
            directors[movie_director] = list()
        directors[movie_director].append(movie_id)

        # Add movies
        title = row[1]
        release_year = row[6]
        movie = Movie(title, release_year)
        movie.votes = row[9]
        movie.metascore = row[11]
        movie.rating = row[8]
        movie.description = row[3]
        movie.id = row[0]

        repo.add_movie(movie)

    for g in genres.keys():
        genre = Genre(g)
        for movie_id in genres[g]:
            movie = repo.get_movie(movie_id)
            if genre.is_related(movie):
                raise AnException
            genre.add_movie(movie)
            movie.add_genre(genre)

        repo.add_genre(genre)

    for a in actors.keys():
        actor = Actor(a)
        for movie_id in actors[a]:
            movie = repo.get_movie(movie_id)
            if actor.is_related(movie):
                raise AnException
            actor.add_movie(movie)
            movie.add_actor(actor)

        repo.add_actor(actor)

    for d in directors.keys():
        director = Director(d)
        for movie_id in directors[d]:
            movie = repo.get_movie(movie_id)
            if director.is_related(movie):
                raise AnException
            director.add_movie(movie)

        repo.add_director(director)


class AnException(Exception):
    pass
