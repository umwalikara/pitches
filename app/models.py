from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    categories=db.relationship('Category',backref = 'user',lazy="dynamic")

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(pitch_id=id).all()
        return comments

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")

    def save_pitch(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
       
        return Pitch.query.all()

    @classmethod
    def get_pitches_by_category(cls,cat_id):
        
        return Pitch.query.filter_by(category_id= cat_id)


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments

class Category(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='categories'


    id = db.Column(db.Integer, primary_key=True)
    category_description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    @classmethod
    def get_categories(cls):
        
        categories = Category.query.all()
        return categories 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))