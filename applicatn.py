import os

from flask import Flask, render_template, request


from flask import Flask, session,url_for,redirect
from flask import flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from udb import *
from  datetime import datetime



app = Flask(__name__, template_folder=r"C:\Users\DELL\Desktop\project1\templates")
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():    
    return render_template('index1.html')

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return "please submit the form"
    else:
        Users.query.all()
        name = request.form.get("name")
        password = request.form.get("password")
        userdata = Users(username=name, password=password, timestamp=str(datetime.now()))
        print(f"added the user {name}{password}******************************************************")
        try:
            db.session.add(userdata)
            db.session.commit()
            return render_template("registered.html", name=name, password=password)
        except Exception :
	        return render_template("error.html", error = "Registration not succesfull")

@app.route("/admin")

def Member():
      """List all users."""
     
      userlist = Users.query.all()
      return render_template("users.html", Users=userlist)


@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    Users.query.all()
    name = request.form.get("name")
    password = request.form.get("password")
    
    try:
        Member = db.session.query(Users).filter(Users.username == username).all()
        print(Member[0].username)
        # session['username'] = request.form.get("Email")
        # return redirect(url_for('indexed'))  
        return render_template("users.html") 
    
    except Exception :
	    return render_template("error.html", errors = "Details are already given")
        


 


# if __name__ == '__main__': 
#     app.run()

