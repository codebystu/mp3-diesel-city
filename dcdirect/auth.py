from flask import render_template, Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login")
def signup():
    return render_template("login.html")