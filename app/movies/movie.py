from flask import Blueprint, render_template, request, url_for

import app.utilities as util
import app.adapters.repository as repo
import app.movies.services as services

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movies_by_genres', methods=['GET'])
def movie_by_genre():
    movie_per_page = 3

    # Read query parameters.
    genre_name = request.args.get('genre')
    actor_name = request.args.get('actor')
    director_name = request.args.get('director')
    # pagination cursor
    cursor = request.args.get('cursor')

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    if genre_name:
        genre_name = genre_name.strip()
    else:
        genre_name = ''
    # if actor_name:
    #     actor_name = actor_name.strip()
    # else:
    #     actor_name = ''
    # if director_name:
    #     director_name = director_name.strip()
    # else:
    #     director_name = ''

    movie_ids = util.get_movie_ids_for_genre(genre_name, repo.repository_instance)

    movies = util.get_movie_ids_for_genre(movie_ids[cursor:cursor + movie_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        # There are preceding movies, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_movie_url = url_for('movie_bp.movies_by_genres', tag=genre_name, cursor=cursor - movie_per_page)
        first_movie_url = url_for('movie_bp.movies_by_genres', tag=genre_name)

    if cursor + movie_per_page < len(movie_ids):
        # There are further movies, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('movie_bp.movies_by_genres', tag=genre_name, cursor=cursor + movie_per_page)

        last_cursor = movie_per_page * int(len(movie_ids) / movie_per_page)
        if len(movie_ids) % movie_per_page == 0:
            last_cursor -= movie_per_page
        last_movie_url = url_for('movie_bp.movies_by_genres', tag=genre_name, cursor=last_cursor)

    return render_template(
        'movies/movies.html',
        title='movies',
        movie_title='Movies tagged by ' + genre_name,
        movies=movies,
        movie_urls=services.get_tags_and_urls(),

        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
    )
