from flask_wtf import FlaskForm
from wtforms import StringField,  TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms.validators import InputRequired, DataRequired, Email 
from flask import Flask, render_template, flash, session, redirect, url_for


class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired('Firstname is required')])
    lastname = StringField('Lastname', validators=[DataRequired('Lastname is required')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired('Gender is required')])
    email = StringField('email', validators = [DataRequired("Your email is required"), Email("Email only!")])
    location = StringField('Location', validators=[DataRequired('Location is required')])
    biography = TextAreaField('Biography', validators = [DataRequired("Biography is required")])
    upload = FileField('images', validators=[FileRequired("Please input file"),FileAllowed(['jpg','png','jpeg'], 'Only jpg,jpeg and png images can be uploaded!')])
    button = SubmitField('Add Profile')