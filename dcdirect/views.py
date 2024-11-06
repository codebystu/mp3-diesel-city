from flask import render_template, Blueprint
from flask_login import login_required, current_user
from dcdirect import app, db
from dcdirect.models import Venue, Food, Event, User

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

@views.route("/myplaces")
def myplaces():
    return render_template("myplaces.html")

@views.route("/myevents")
def myevents():
    return render_template("myevents.html")

@views.route("/myfood")
def myfood():
    return render_template("myfood.html")


    