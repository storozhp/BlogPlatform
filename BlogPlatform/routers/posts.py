from flask import Blueprint, render_template, request, flash, redirect, url_for
from BlogPlatform.jwt import token_required
from BlogPlatform.models import Post


posts_router = Blueprint("posts_router", __name__)


@posts_router.route("/new_post", methods=["GET", "POST"])
@token_required
def new_post(current_user):
    if request.method == "POST":
        author = current_user['username']
        title = request.form['post_title']
        content = request.form['post_content']
        Post.create_post(author, title, content)
        flash('Post created', 'success')
        return redirect(url_for('main_router.index'))

    return render_template("new_post.html")


@posts_router.route("/post/<post_id>")
def post(post_id):
    post = Post.get_post_by_id(post_id)
    return render_template('post.html', post=post)


@posts_router.route("/delete_post/<post_id>")
@token_required
def delete_post(current_user, post_id):
    post = Post.get_post_by_id(post_id)

    if current_user['username'] != post['post_author']:
        flash("You are not post author", "error")
    else:
        Post.delete_post(post_id)
    
    return redirect(url_for('main_router.index'))
