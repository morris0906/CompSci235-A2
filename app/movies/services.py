from flask import Blueprint, url_for

import app.adapters.repository as repo
import app.utilities as util


# Configure Blueprint.
services_blueprint = Blueprint(
    'services_bp', __name__)


def get_genres_and_urls():
    genre_names = util.get_genre_names(repo.repo_instance)
    genre_urls = dict()
    for genre_name in genre_names:
        genre_urls[genre_name] = url_for('movie_bp.movies_by_genres', genre=genre_name)

    return genre_urls


def get_selected_movies(quantity=3):
    articles = util.get_movies_random(quantity, repo.repo_instance)

    for article in articles:
        article['hyperlink'] = url_for('news_bp.articles_by_date', date=article['date'].isoformat())
    return articles
