from flask import Blueprint, render_template
from BlogPlatform.models import Post, User
from BlogPlatform.jwt import token_required


main_router = Blueprint("main_router", __name__)


@main_router.route("/")
def index():
    posts = Post.get_all_posts()
    return render_template("index.html", posts=posts)

@main_router.route("/profile/<username>")
@token_required
def profile(current_user, username):
    user = User.find_by_username(username)
    user_posts = Post.get_user_posts(username)
    return render_template("profile.html", user=user, user_posts=user_posts)