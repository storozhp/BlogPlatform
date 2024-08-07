import datetime
import jwt

from os import getenv
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from BlogPlatform.models import User

main = Blueprint('main', __name__)
load_dotenv()


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.find_by_username(username):
            flash("User already exists", "danger")
            redirect(url_for("main.register"))
        else:
            User.create_user(username, password)
            flash("Successfully registered", "success")
            return redirect(url_for("main.login"))

    return render_template("register.html")


@main.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)

        if user and User.verify_password(user['password'], password):
            token = jwt.encode({
                'username': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)
            }, getenv("SECRET_KEY"), algorithm="HS256")

            session['token'] = token
            session['username'] = username

            flash("Login successful", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Incorrect username/password", "danger")
            return redirect(url_for("main.login"))

    return render_template("login.html")


@main.route("/logout")
def logout():
    session.pop('token', None)
    session.pop('username', None)
    flash("You logged out", "success")
    return redirect(url_for("main.index"))
