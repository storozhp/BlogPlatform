import jwt
from os import getenv
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv
from BlogPlatform.models import User

load_dotenv()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('access-token')
        if not token:
            return jsonify({"message": "Token not found"}), 401
        try:
            data = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
            current_user = User.find_by_username(data['username'])
        except:
            return jsonify({"message": "Token invalid"}), 401
        return f(current_user, *args, **kwargs)

    return decorated
