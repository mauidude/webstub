import os
env = os.environ.get('FLASK_ENV', 'DEVELOPMENT')

CSRF_ENABLED=True
SECRET_KEY='622fa765fa110611a164164fa347e941687cb7711c4ad6f1017a448cdd4c8c64'
DEBUG=True
TESTING=True

if env == 'PRODUCTION':
  from pymongo.uri_parser import parse_uri

  uri = os.environ['MONGOHQ_URL']
  parsed = parse_uri(uri)

  host, port = parsed.get('nodelist')[0]

  MONGODB_SETTINGS = {
    'DB': parsed.get('database'),
    'HOST': host,
    'PORT': port,
    'USERNAME': parsed.get('username'),
    'PASSWORD': parsed.get('password')
  }
else:
  MONGODB_SETTINGS = {
    'DB': 'webstub',
    'HOST': 'localhost'
  }
