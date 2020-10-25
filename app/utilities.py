# import random
from app.adapters.repository import AbstractRepository


# def get_movies_random(quantity, repo: AbstractRepository):
#     movies = random.sample(range(0, repo.get_number_of_movies() - 1), quantity)
#     movie_list = []
#     for movie in movies:
#         movie_list.append(repo.get_movie()[movie])
#    return movie_list


def get_actors(repo: AbstractRepository):
    actors = repo.get_actors()
    actors_list = [actor.actor_full_name for actor in actors]

    return actors_list


def get_genres(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names


def get_director(repo: AbstractRepository):
    director = repo.get_directors()
    directors = [d.director_full_name for d in director]

    return directors
