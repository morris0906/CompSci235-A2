"""Initialize Flask app."""

import os

from flask import Flask
import app.adapters.repository as repo
from app.adapters.memory_repository import *


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('movie', 'adapters', 'data', 'Data1000Movies.csv')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    @app.route('/')
    def home():
        return "Welcome!"

    return app
