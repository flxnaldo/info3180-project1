"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Arnoldo Daley")

@app.route('/property', methods=["GET", "POST"])
def property():
    pf = PropertyForm()
    if request.method == 'POST':
        if pf.validate_on_submit():
            title = pf.title.data
            num_bedrooms = pf.num_bedrooms.data
            num_bathrooms = pf.num_bathrooms.data
            location = pf.location.data
            price = pf.price.data
            property_type = pf.property_type.data
            description = pf.description.data
            photo = photo_save(pf.photo.data)

            property_info = Property(title, num_bedrooms, num_bathrooms, location, price, property_type, description, photo)
            db.session.add(property_info)
            db.session.commit()
            flash('Property Added', 'success')
            return redirect(url_for('properties'))
    else:
        flash_errors(pf)
    return render_template('propertyADD.html', form=pf)

@app.route('/property/<propertyid>')
def aproperty(propertyid):
    a_property = db.session.query(Property).filter(Property.id == propertyid).first()
    return render_template('aproperty.html', crib=a_property)

@app.route('/properties')
def properties():
    cribs = db.session.query(Property).all()
    return render_template('allproperties.html', cribs = cribs)


@app.route('/app/static/uploads/<filename>')
def get_image(filename):
    rootdir_ = os.getcwd()
    return send_from_directory(os.path.join(rootdir_,app.config['UPLOAD_FOLDER']), filename)


def photo_save(photo):
    fn = secure_filename(photo.filename)
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
    return fn

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
