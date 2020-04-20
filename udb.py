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
