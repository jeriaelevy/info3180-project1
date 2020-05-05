  


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost/infoproj_db_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

app.config.from_object(__name__)

from app import views