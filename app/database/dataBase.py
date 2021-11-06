from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)
    cellPhone = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return '<User %r>'% self.username
    
    def onGetSetPassword(self, password):
        self.password = generate_password_hash(password)

    def onGetCheckPassword(self, password):
        return check_password_hash(self.password, password)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Idea(db.Model):
    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    isPublic = db.Column(db.Boolean, default=False)
    categoryId = db.Column(db.Integer, db.ForeignKey('categories.id',ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category',backref=db.backref('ideas',lazy=True))
    userId = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('ideas',lazy=True))