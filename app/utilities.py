import random
from app.adapters.repository import AbstractRepository
from app.adapters.memory_repository import MemoryRepository


def get_movies_random(quantity, repo: AbstractRepository):
    movies = random.sample(range(0, repo.get_number_of_movies() - 1), quantity)
    movie_list = []
    for movie in movies:
        movie_list.append(repo.get_movie()[movie])
    return movie_list


def get_movie_ids_for_genre(genre, repo: AbstractRepository):
    movie_id = repo.get_movies_for_genre(genre)

    return movie_id


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names
