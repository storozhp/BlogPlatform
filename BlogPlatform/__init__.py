from flask import Flask
from os import getenv
from dotenv import load_dotenv
from BlogPlatform import routes, database


load_dotenv()


app = Flask(__name__)
app.config["SESSION_TYPE"] = 'memcached'
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

app.register_blueprint(routes.main)
