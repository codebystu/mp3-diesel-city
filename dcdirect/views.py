from flask import render_template, Blueprint
from dcdirect import app, db
from dcdirect.models import Business, Category, Event

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("events.html")

@views.route("/places")
def places():
    return render_template("places.html")  

@views.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html")


    