# module to set up a basic Flask application
from flask import Flask
from .extensions import db
from .routes import short


def create_app(config_file="settings.py"):
    # build the Flask name
    app = Flask(__name__)

    # configure it using the settings.py file
    app.config.from_pyfile(config_file)

    # initialize the database
    db.init_app(app)

    # register all the routes for the application
    app.register_blueprint(short)
    return app
