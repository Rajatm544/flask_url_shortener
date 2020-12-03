import string
from .extensions import db
from datetime import datetime
from random import choices


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
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

        # ensure that the short_url is unique, by checking with the model db
        link = self.query.filter_by(short_url=short_url).first()

        # if the link exists, call this function again, else return the new link
        if link:
            return self.generate_short_url()

        return link
