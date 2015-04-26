from app import db
from passlib.apps import custom_app_context as pwd_context
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    gender = db.Column(db.String(1))
    fav_food =  db.Column(db.String(50))
    #about = db.Column(db.String(300), index = True, unique = False)
    date_joined =  db.Column(db.String(8), index = True, unique =  False)
    #role =  db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return unicode(self.id)

    def hash_password(self, password):
        self.password_hash = pwd.context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Restaurant(db.Model):
	
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(120), index = True, unique = True)
    hours =  db.Column(db.String(20), index = True, unique = True)
    location = db.Column(db.String(120), index = True, unique = True)
    price_rng = db.Column(db.String(5), index = True, unique = True)
    #ratings feed, can I add a dictionary or array of feeds to the db?
    #reviews
    #profile image
    phone = db.Column(db.Integer, index =  True, unique = True)
    #parking: yes or no
    #credit card: yes or no
    #Bar/Alcohol: yes or no
    #ambience: familiar, casual, fine dining, buffet, fast casual, cafe, franchise, food truck, catering, ethnic
    #attire: casual, fancy, gimmick

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
