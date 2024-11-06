from dcdirect import db
from flask_login import UserMixin



class Venue(db.Model):
    # schema for venue model
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(50), unique=True, nullable=False)
    venue_address = db.Column(db.String(200), unique=False, nullable=False)
    contact_number = db.Column(db.Integer, unique=False, nullable=True)
    serves_food = db.Column(db.Boolean, default=False)
    venue_description = db.Column(db.Text, unique=False, nullable=True)
    food_id = db.Column(db.Integer, db.ForeignKey("food.id"), nullable=False)
    event_id = db.relationship("Event", backref="venue", cascade="all, delete", lazy=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    def __repr__(self):
        return self.venue_name


class Food(db.Model):
    # schema for food model
    id = db.Column(db.Integer, primary_key=True)
    food_type = db.Column(db.String(20), unique=True, nullable=False)
    business_name = db.relationship("Venue", backref="food", lazy=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return self.food_name


class Event(db.Model):
    # schema for event model
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), unique=False, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id", ondelete="CASCADE"), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    event_description = db.Column(db.Text, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return "#{0} - Event: {1} | Venue: {2} | Date: {3} | Description: {4}".format(
            self.id, self.event_name, self.venue_id, self.date_time, self.event_description
        )

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    # schema for users model
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    venues = db.relationship('Venue', backref="users", cascade="all, delete", lazy=True)
    foods = db.relationship('Food', backref="users", cascade="all, delete", lazy=True)
    events = db.relationship('Event', backref="users", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.id