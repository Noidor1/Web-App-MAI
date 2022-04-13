from flask import Flask

app = Flask(__name__)

from .routes import hello_world_route
from .routes import users_route
