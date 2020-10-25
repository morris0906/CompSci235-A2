from typing import Iterable

from app.adapters.repository import AbstractRepository
from app.domainmodel.movie import Movie
from app.domainmodel.actor import Actor
from app.domainmodel.genre import Genre
from app.domainmodel.director import Director


class NoneException(Exception):
    pass


def get_movie(id: int, repo: AbstractRepository):
    movie = repo.get_movie(id)

    if movie is None:
        raise NoneException

    return movie_to_dict(movie)


def get_movie_ids(repo: AbstractRepository):
    movie_ids = repo.get_movies_id_all()
    return movie_ids


def get_movie_ids_genre(genre, repo: AbstractRepository):
    movie_ids = repo.get_movies_for_genre(genre)
    return movie_ids


def get_movie_ids_actor(actor, repo: AbstractRepository):
    movie_ids = repo.get_movies_for_actor(actor)
    return movie_ids


def get_movie_ids_director(director, repo: AbstractRepository):
    movie_ids = repo.get_movies_for_director(director)
    return movie_ids


def get_movies_by_id(ids, repo: AbstractRepository):
    movies = repo.get_movies_by_id(ids)
    movies_dict = movies_to_dict(movies)
    return movies_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def genre_to_dict(genre: Genre):
    genre_dict = {'type': genre.genre_name, 'genre_movies': [movie.id for movie in genre.genre_movies]}
    return genre_dict


def genres_to_dict(genres: Iterable[Genre]):
    return [genre_to_dict(genre) for genre in genres]


def actor_to_dict(actor: Actor):
    actor_dict = {'name': actor.actor_full_name, 'actor_movies': [movie.id for movie in actor.actor_movies]}
    return actor_dict


def actors_to_dict(actors: Iterable[Actor]):
    return [actors_to_dict(actor) for actor in actors]


def director_to_dict(director: Director):
    direct_dict = {'name': director.director_full_name,
                   'director_movies': [movie.id for movie in director.director_movies]}
    return direct_dict


def directors_to_dict(directors: Iterable[Director]):
    return [director_to_dict(director) for director in directors]


def movie_to_dict(movie: Movie):
    movie_dict = {'id': movie.id,
                  'title': movie.title,
                  'description': movie.description,
                  'year': movie.year,
                  'runtime_minutes': movie.runtime_minutes,
                  'rating': movie.rating,
                  'votes': movie.votes,
                  'meta_score': movie.metascore,
                  'genres': genres_to_dict(movie.genres),
                  'actors': actors_to_dict(movie.actors),
                  'directors': director_to_dict(movie.director)
    }
