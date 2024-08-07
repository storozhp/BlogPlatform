from flask import Blueprint, render_template
from BlogPlatform.models import Post
from BlogPlatform.database import posts_collection


main_router = Blueprint("main_router", __name__)


@main_router.route("/")
def index():
    posts = Post.get_all_posts()
    return render_template("index.html", posts=posts)
