import datetime
import jwt

from os import getenv
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from BlogPlatform.jwt import token_required
from BlogPlatform.models import User

auth_router = Blueprint('auth_router', __name__)
load_dotenv()


@auth_router.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.find_by_username(username):
            flash("User already exists", "error")
            redirect(url_for("auth_router.register"))
        else:
            User.create_user(username, password)
            flash("Successfully registered", "success")
            return redirect(url_for("auth_router.login"))

    return render_template("register.html")


@auth_router.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)

        if user and User.verify_password(user['password'], password):
            token = jwt.encode({
                'username': username,
                'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=8)
            }, getenv("SECRET_KEY"), algorithm="HS256")

            session['token'] = token
            session['username'] = username

            flash("Login successful", "success")
            return redirect(url_for("main_router.index"))
        else:
            flash("Incorrect username/password", "error")
            return redirect(url_for("auth_router.login"))

    return render_template("login.html")


@auth_router.route("/logout")
def logout():
    if session.get('token'):
        session.pop('token', None)
        session.pop('username', None)
        flash("You logged out", "success")
        return redirect(url_for("main_router.index"))
    else:
        flash("You are not logged", "error")
        return redirect(url_for('auth_router.login'))
