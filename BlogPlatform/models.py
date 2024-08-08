from BlogPlatform.database import users_collection, posts_collection
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId


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
    @staticmethod
    def create_post(author_username: str, post_title:str, post_content:str):
        posts_collection.insert_one({
            "post_author": author_username,
            "post_title": post_title,
            "post_content": post_content
        })

    @staticmethod
    def get_post_by_id(post_id):
        return posts_collection.find_one({
            "_id": ObjectId(post_id)
        })

    @staticmethod
    def get_all_posts():
        return list(posts_collection.find())
    
    @staticmethod
    def get_user_posts(username):
        return list(posts_collection.find({"post_author": username}))
    
    @staticmethod
    def delete_post(post_id):
        posts_collection.find_one_and_delete({"_id": ObjectId(post_id)})
