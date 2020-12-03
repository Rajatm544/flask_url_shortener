from flask import Blueprint, render_template, request

from .extensions import db
from .models import Link

short = Blueprint("short", __name__)


@short.route("/<short_url>")
def redirect_to_url(short_url):
    pass


@short.route("/")
def index():
    return render_template("index.html")


@short.route("/visits")
def visits():
    pass


@short.route("/new", methods=["POST"])
def new_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    return render_template("link_added.html", new_link=link.short_url, original_url=link.original_url)


@short.errorhandler(404)
def page_not_found(e):
    return "", 404
