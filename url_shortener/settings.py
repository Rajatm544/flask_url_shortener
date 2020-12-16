# Settings for the SQLite Database
import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
