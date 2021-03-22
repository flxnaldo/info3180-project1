from . import db

class Property(db.Model):

    __tablename__ = 'house_properties'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    num_bedrooms = db.Column(db.String())
    num_bathrooms=db.Column(db.String())
    location = db.Column(db.String())
    price = db.Column(db.String())
    property_type = db.Column(db.String())
    description = db.Column(db.String(), unique=True)
    photo = db.Column(db.String())
    

    def __init__(self, title, num_bedrooms, num_bathrooms, location, price, property_type, description, photo):
        self.title=title
        self.num_bedrooms=num_bedrooms
        self.num_bathrooms=num_bathrooms
        self.location=location
        self.price=price
        self.property_type=property_type
        self.description=description
        self.photo=photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)