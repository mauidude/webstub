import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_object('config')

print 'Loading MongoEngine...'
db = MongoEngine(app)

print 'MongoEngine loaded'

from app import views