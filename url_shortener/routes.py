from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Link

short = Blueprint("short", __name__)

# A route to redirect all pages with any String character to corresponding original link


@short.route("/<short_url>")
def redirect_to_url(short_url):

    # query the db to fetch the record corresponding to this current unique String
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    return redirect(link.original_url)

# home page to display form input


@short.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@short.route("/visits")
def visits():
    links = Link.query.all()
    return render_template("visits.html", links=links)

# route to handle form data and store new


@short.route("/", methods=["POST"])
def new_link():
    original_url = request.form['original_url']
    # check if link is already stored in the database
    link = Link.query.filter_by(original_url=original_url).first()
    if not link:
        link = Link(original_url=original_url)
        db.session.add(link)
        db.session.commit()

    # display the home page along with the details for the shortened URL
    return render_template("index.html", short_link=link.short_url, original_link=link.original_url, visits=link.visits)

# handle 404 errors


@short.errorhandler(404)
def page_not_found(e):
    return "<h1>404. Page Not Found</h1>", 404
