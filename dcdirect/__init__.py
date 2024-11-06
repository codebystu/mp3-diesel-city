import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .database import db
from .models import User
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db.init_app(app)

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'views.home'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))