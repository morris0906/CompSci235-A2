from flask import Blueprint,render_template

import app.utilities as util

home_blueprint = Blueprint('home_bp', __name__)

@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_movies=util.get_movies_random(5)
    )
