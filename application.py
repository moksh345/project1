from flask import Flask, render_template, request

app = Flask(_name_, template_folder=r"C:\Users\DELL\Desktop\project1\templates")

@app.route("/")
def home():    
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("user")
    password = request.form.get("password")    
    return render_template("register.html", name=name, password=password)

if _name_ == '_main_': 
    app.run()

