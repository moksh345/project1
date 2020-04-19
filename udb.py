from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    username =db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp=db.Column(db.String, nullable=False)
