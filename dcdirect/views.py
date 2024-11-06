from flask import render_template, Blueprint
from flask_login import login_required, current_user
from dcdirect import app, db
from dcdirect.models import Venue, Food, Event, User

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("events.html", user=current_user)

@views.route("/places")
def places():
    return render_template("places.html", user=current_user)  

@views.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html", user=current_user)

@views.route("/myplaces")
@login_required
def myplaces():
    return render_template("myplaces.html", user=current_user)

@views.route("/myevents")
@login_required
def myevents():
    return render_template("myevents.html", user=current_user)

@views.route("/myfood")
@login_required
def myfood():
    return render_template("myfood.html", user=current_user)


    