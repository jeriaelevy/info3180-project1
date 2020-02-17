
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField



class ContactForm(FlaskForm):
    name = StringField('Name (Required)')
    email = StringField('Email (Required)')
    subject = StringField('Subject (Required)')
    message = StringField('Message (Required)')
    submit = SubmitField('Send')








