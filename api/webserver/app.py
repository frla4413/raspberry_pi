''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''
from flask import Flask, render_template, url_for,request, redirect, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sensor import sensor
from sensors_webpage.sensors_webpage import sensors_webpage

app = Flask(__name__)
app.secret_key = "jagatergodisvarjedag"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

app.register_blueprint(sensors_webpage,url_prefix="/sensors")

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.email}"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        found_user =  Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user,None)
            db.session.add(usr)
            db.session.commit()

        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Alread logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user =  Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email)
    else:
        flash("You are not logged in", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    user = session["user"]
    msg = "You have been logged out, " + user + "!"
    flash(msg, "info")
    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=Users.query.all())

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=80, debug=True)
