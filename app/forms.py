from flask.ext.mongoengine.wtf import model_form
from app.models import Endpoint

EndpointForm = model_form(Endpoint)
