from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    bio = db.Column(db.String(255))
    photo_data = db.Column(db.LargeBinary)
    username = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, server_default=db.func.now())

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genderTypes = db.Column(db.String(80))


    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        try:
            return unicode(self.id) # python 2
        except NameError:
            return str(self.id) # python 3
    def __repr__(self):
        return '<User %r>' % (self.username) 