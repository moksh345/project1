from flask import Flask, render_template, request

app = Flask(__name__, template_folder=r"C:\Users\DELL\Desktop\project1\templates")

@app.route("/")
def home():    
    return render_template('index1.html')

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return "please submit the form"
    else:
        name = request.form.get("name")
        password = request.form.get("password")    
        return render_template("registered.html", name=name)

if __name__ == '__main__': 
    app.run()

