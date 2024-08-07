import jwt
from os import getenv
from flask import request, flash, redirect, url_for
from functools import wraps
from dotenv import load_dotenv
from BlogPlatform.models import User

load_dotenv()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('access-token')
        if not token:
            flash("Token not found", "error")
            return redirect(url_for("main.login"))
        try:
            data = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
            current_user = User.find_by_username(data['username'])
        except:
            flash("Token invalid", "error")
            return redirect(url_for("main.login"))
        return f(current_user, *args, **kwargs)

    return decorated
