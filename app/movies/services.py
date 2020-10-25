from flask import Blueprint, url_for

import app.adapters.repository as repo
import app.utilities as util

# Configure Blueprint.
services_blueprint = Blueprint(
    'services_bp', __name__)


def get_genres_and_urls():
    genres_name = util.get_genres(repo.repo_instance)
    genre_url = dict()
    for genre in genres_name:
        genre_url[genre] = url_for('movie_bp.movie_by_genres', genre=genre)

    return genre_url


def get_actors_and_urls():
    actors = util.get_genres(repo.repo_instance)
    actor_url = dict()
    for actor in actors:
        actor_url[actor] = url_for('movie_bp.movie_by_genres', actor=actor)

    return actor_url


def get_director_and_urls():
    directors = util.get_genres(repo.repo_instance)
    director_url = dict()
    for director in directors:
        director_url[director] = url_for('movie_bp.movie_by_genres', director=director)

    return director_url

# def get_selected_movies(quantity=3):
#     articles = util.get_movies_random(quantity, repo.repository_instance)
#
#     for article in articles:
#         article['hyperlink'] = url_for('news_bp.articles_by_date', date=article['date'].informant())
#     return articles
