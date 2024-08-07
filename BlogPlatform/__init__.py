from flask import Flask
from os import getenv
from dotenv import load_dotenv
from BlogPlatform import database
from BlogPlatform.routers import main, auth, posts


load_dotenv()


app = Flask(__name__)
app.config["SESSION_TYPE"] = 'memcached'
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

app.register_blueprint(main.main_router)
app.register_blueprint(auth.auth_router)
app.register_blueprint(posts.posts_router)
