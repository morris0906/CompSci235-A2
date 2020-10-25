"""Initialize Flask app."""
import os

from flask import Flask

import app.adapters.repository as repo
from app.adapters.memory_repository import MemoryRepository, load_users, load_movies


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')

    data_path = os.path.join('app', 'datafiles', 'Data1000Movies.csv')
    data_path2 = os.path.join('app', 'datafiles', 'users.csv')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # create memory repository
    repo.repo_instance = MemoryRepository()
    load_movies(data_path, repo.repo_instance)
    load_users(data_path2, repo.repo_instance)

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import movie
        app.register_blueprint(movie.movie_blueprint)

        from .movies import services
        app.register_blueprint(services.services_blueprint)

    return app
