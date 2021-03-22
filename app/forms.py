from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    num_bedrooms = StringField('No. of Rooms', validators=[InputRequired()])
    num_bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = StringField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])

