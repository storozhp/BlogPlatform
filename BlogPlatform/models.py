from BlogPlatform.database import users_collection
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    @staticmethod
    def create_user(username: str, password: str):
        hashed_password = generate_password_hash(password)

        user_model = {
            "username": username,
            "password": hashed_password,
        }

        users_collection.insert_one(user_model)

    @staticmethod
    def find_by_username(username: str):
        return users_collection.find_one({"username": username})

    @staticmethod
    def verify_password(hashed_password: str, password: str):
        return check_password_hash(pwhash=hashed_password, password=password)


class Post:
    pass
