"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
from wtforms.validators import DataRequired
from .forms import ProfileForm
from app.models import UserProfile
import os
from werkzeug.utils import secure_filename
from datetime import datetime

###
# Routing for your application.
###

# app.config['SECRET_KEY'] = 'thecodex'
UPLOAD_FOLDER = '/Users/Jeria/Documents/Projects/info3180-project1/app/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jeria Levy")
    
@app.route('/profile/', methods=['GET'])
def profile():
    """Render the website's about page."""
    profileForm = ProfileForm()
    error = None
    return render_template('profile.html', name="Profile", form=profileForm, error=error)

@app.route('/profiles/')
def profiles():

    results = []

    profiles = db.session.query(UserProfile)

    results = profiles.all()

    return render_template('profiles.html', name="UWI Students", profiles=results, len=results)

@app.route('/view-profile/<id>')
def viewProfile(id):



    getMyId = id
    myProfile = UserProfile.query.filter_by(id=getMyId).first()

    dateClean = datetime.strftime(myProfile.created_on, '%B %d, %Y')
    
    return render_template('view.html', myProfile=myProfile, acc_created=dateClean)
 
@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = ProfileForm()

    # if form.validate_on_submit():

    if request.method == 'POST':

        req = request.form

        file = request.files.get('photo')

        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_profile = UserProfile(
            firstname = req.get('firstName'),
            lastname = req.get('lastName'),
            email = req.get('email'),
            bio = req.get('biography'),
            location = req.get('location'),
            photo = file.filename,
            gender = req.get('gender'),
            photo_data = file.read()
        )   

        db.session.add(new_profile)
        db.session.commit()
        return redirect(url_for('profiles'))
    else:
        return redirect(url_for('profile'))


    # return render_template('submit.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
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
    app.run(debug=True, host="0.0.0.0", port="8080")
