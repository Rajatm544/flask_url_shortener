# file to setup the Schema of the data stored in the database
import string
from .extensions import db
from datetime import datetime
from random import choices


class Link(db.Model):

    # define all the fields to store data

    # A unique Id is mandatory for all database records
    id = db.Column(db.Integer, primary_key=True)

    # The original link is stored as a string of maximum 512 characters
    original_url = db.Column(db.String(512))

    # The unique String of 5 characters
    short_url = db.Column(db.String(5), unique=True)

    # An integer to store the number of visits
    visits = db.Column(db.Integer, default=0)

    # Date at which this record was created
    date_created = db.Column(db.DateTime, default=datetime.now)

    # generate the short_file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):

        # the entire list of a-z, A-Z, 0-9
        characters = string.digits + string.ascii_letters

        # choose any 5 random characters from the list
        short_url = "".join(choices(characters, k=5))

        # ensure that the short_url is unique, by querying the db
        link = self.query.filter_by(short_url=short_url).first()

        # if the link exists, call this function again, else return the new link
        if link:
            return self.generate_short_url()

        return short_url
