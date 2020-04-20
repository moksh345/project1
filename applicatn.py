import os

from flask import Flask, render_template, request


from flask import Flask, session,url_for,redirect
from flask import flash
from flask_session import Session
from sqlalchemy import create_engine,desc
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
    return render_template('index1.html',message="")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return "please submit the form"
    else:
        Users.query.all()
        name = request.form.get("name")
        password = request.form.get("password")
        userdata = Users(username=name, password=password)
        # print(f"added the user {name}{password}, timestamp=str(datetime.now())******************************************************")
        try:
            db.session.add(userdata)
            db.session.commit()
            # Registration is succesfull page is shown
            return render_template("registered.html", name=name, password=password)
        except Exception :
	        return render_template("error.html", error = "Registration not succesfull")

@app.route("/admin")

def Member():
      """List all users."""
     
      userlist = Users.query.order_by(desc(Users.timestamp)).all()
      return render_template("users.html", Users=userlist)


@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    if request.method == "GET":
        return "please submit the form/ Invalid login request"
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        userdata = Users.query.filter_by(username=name).first()
        if userdata is not None:
            # validate username and password
            if userdata.username == name and userdata.password == password:
                # adding the username as session variable
                session[name] = name
                return render_template("login.html", name=name)
            # user verification failed
            else:
                return render_template("index1.html", message="Invalid username/password.")
        # new user
        else:
            return render_template("index1.html", message="You have not registered. Please register to login.")
            
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop(name, None)
   return redirect(url_for('home'))



    # Users.query.all()
    # name = request.form.get("name")
    # password = request.form.get("password")
    
    # try:
    #     Member = db.session.query(Users).filter(Users.username == username).all()
    #     print(Member[0].username)
    #     # session['username'] = request.form.get("Email")
    #     # return redirect(url_for('indexed'))  
    #     return render_template("users.html") 
    
    # except Exception :
	#     return render_template("error.html", errors = "Details are already given")
        


 


# if __name__ == '__main__': 
#     app.run()

