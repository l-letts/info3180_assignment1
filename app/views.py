"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, upload_f, Allowed_Uploads 
from flask import render_template, request, redirect, url_for, flash,session, abort, send_from_directory
from models import UserProfile
from forms import ProfileForm
from werkzeug.utils import secure_filename
import os
import datetime


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
    return render_template('about.html')
    
@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        gender = form.gender.data
        email =  form.email.data
        location = form.location.data
        biography = form.biography.data
        file = form.upload.data
        datecreated = str(datetime.date.today())
        
        Filename = secure_filename(file.filename)
        user = UserProfile(firstname,lastname,gender,email,location,biography,Filename,datecreated)
        db.session.add(user)
        db.session.commit()
        file.save(os.path.join(upload_f, Filename))
        flash('Successfully added.', 'success')
        return redirect(url_for('profiles')) 
    return render_template("profile.html", form=form)
        
    
def get_uploaded_images():
    Images = []
    Load_files = os.listdir('./app/static/uploads/')
    for file in Load_files:
        if file.split('.')[-1] in Allowed_Uploads:
            Images.append(file)
    return Images



@app.route('/profiles/')
def profiles():
    images_names = get_uploaded_images()
    users = UserProfile.query.all()
    return render_template("profiles.html", users=users, images_names=images_names)
    
    
@app.route("/profiles/<id>")
def user_profile(id):
    user = UserProfile.query.filter_by(id=id).first()
    image_names= get_uploaded_images()
    return render_template('user_profile.html', user=user, image_names=image_names)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
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
