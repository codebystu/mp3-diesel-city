from dcdirect import db


class Business(db.Model):
    # schema for business model
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(50), unique=True, nullable=False)
    business_address = db.Column(db.String(200), unique=False, nullable=False)
    contact_number = db.Column(db.Integer, unique=True, nullable=False)
    event_venue = db.Column(db.Boolean, default=False, nullable=False)
    business_description = db.Column(db.Text, unique=False, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey("subcategory.id"), nullable=False)
    event_id = db.relationship("Event", backref="business", cascade="all, delete", lazy=True)
    def __repr__(self):
        return self.business_name


class Category(db.Model):
    # schema for business category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    subcategory_id = db.relationship("Subcategory", backref="category", lazy=True)
    business_name = db.relationship("Business", backref="category", lazy=True)

    def __repr__(self):
        return self.category_name


class Subcategory(db.Model):
    # schema for business subcategory model
    id = db.Column(db.Integer, primary_key=True)
    subcategory_name = db.Column(db.String(20), unique=True, nullable=False)
    business_name = db.relationship("Business", backref="subcategory", lazy=True)


    def __repr__(self):
        return self.subcategory_name


class Event(db.Model):
    # schema for event model
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), unique=True, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("business.id"), ondelete="CASCADE", nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    event_Description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "#{0} - Event: {1} | Venue: {2} | Date: {3}".format(
            self.id, self.event_name, self.venue_id, self.date_time
        )


class Images(Resource):

