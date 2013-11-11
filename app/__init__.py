import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_environments import Environments

app = Flask(__name__)
env = Environments(app)

env.from_yaml(os.path.join(os.getcwd(), 'config.yaml'))

db = MongoEngine(app)

from app import views