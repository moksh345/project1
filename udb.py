from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import DateTime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    username =db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(DateTime, default=datetime.datetime.now) 
    # db.Column(db.String, nullable=False)

class Books(db.Model):
    __tablename__ = "BOOKS"
    isbn = db.Column(db.String, nullable = False,primary_key=True)
    tittle = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable=False)

class Review(db.Model):
    __tablename__ = "Review"
    username = db.Column(db.String, primary_key=True)
    isbn = db.Column(db.String, nullable=False, primary_key=True)
    rating = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)

