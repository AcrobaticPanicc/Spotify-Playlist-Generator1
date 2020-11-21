from flask import Flask

from app.routes.routes import blueprint
from app.auth.auth import auth_blueprint
from app.fine_tune.fine_tune import fine_tune_blueprint
from app.select_tracks.select_tracks import select_blueprint
from app.result.result import result_blueprint
from app.home.home import home_blueprint
from app.loading.loading import loading_blueprint
from app.error.error import error_blueprint


def create_app():
    """
    Creating and returning the app
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JUSTARANDOMKEY'

    app.register_blueprint(blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(fine_tune_blueprint)
    app.register_blueprint(select_blueprint)
    app.register_blueprint(result_blueprint)
    app.register_blueprint(loading_blueprint)
    app.register_blueprint(error_blueprint)
    return app
