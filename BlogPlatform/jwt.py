import jwt
from os import getenv
from flask import session, flash, redirect, url_for
from functools import wraps
from dotenv import load_dotenv
from BlogPlatform.models import User

load_dotenv()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = session.get('token')
        if not token:
            flash("You are not logged", "error")
            return redirect(url_for("auth_router.login"))
        try:
            data = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
            current_user = User.find_by_username(data['username'])
        except:
            flash("Login failed", "error")
            return redirect(url_for("auth_router.login"))
        return f(current_user, *args, **kwargs)

    return decorated
