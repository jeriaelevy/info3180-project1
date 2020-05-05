
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, SubmitField
from flask_wtf.file import FileField, FileRequired
from flask import Flask
from wtforms.validators import InputRequired, Length, EqualTo, Email



class ContactForm(FlaskForm):
    name = StringField('Name (Required)')
    email = StringField('Email (Required)')
    subject = StringField('Subject (Required)')
    message = StringField('Message (Required)')
    submit = SubmitField('Send')

class ProfileForm(FlaskForm):
    firstName = StringField('First Name (Required)',
            validators=[InputRequired(message="First Name Required"), Length(min=4, max=225)])
    lastName = StringField('Last Name (Required)',
            validators=[InputRequired(message="Last Name Required"), Length(min=4, max=225)])
    gender = SelectField('Gender (Required)', 
            choices = [('none', 'Select Option'), ('Male', 'Male'), ('Female', 'Female')])
    email = StringField('Email (Required)',
            validators=[InputRequired(message="Email Required"), Email(message="Email Required")])
    biography = TextField('Biography (Required)',
            validators=[InputRequired(message="Bio Required")])
    location = StringField('Location (Required)',
            validators=[InputRequired(message="Location Required")])
    photo = FileField(validators=[FileRequired()])










