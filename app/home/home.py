from flask import Blueprint, render_template

import app.movies.services as service

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',

        genre_urls=service.get_genres_and_urls(),
        actor_urls=service.get_actors_and_urls(),
        director_urls=service.get_director_and_urls()
    )
