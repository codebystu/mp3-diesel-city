from flask import render_template
from dcdirect import app, db
from dcdirect.models import Business, Category, Event


@app.route("/")
def home():
    return render_template("events.html")

@app.route("/places")
def places():
    return render_template("places.html")  

@app.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
    