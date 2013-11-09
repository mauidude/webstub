from app import db

class Endpoint(db.Document):
  STATUS_CODES = [200, 400, 401, 403, 404, 500, 501, 503]

  path = db.StringField(required=True, unique=True, help_text='The path of the endpoint')
  status_code = db.IntField(required=True, help_text='The HTTP status code to return', choices=[[c, str(c)] for c in STATUS_CODES])
  latency = db.IntField(help_text='The latency of the request in seconds', default=0)
