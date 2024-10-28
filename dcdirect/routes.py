from flask import render_template
from dcdirect import app, db
from dcdirect.models import Business, Category, Event


@app.route("/")
def home():
    return render_template("events.html")
    