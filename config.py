import os
env = os.environ['FLASK_ENV']

CSRF_ENABLED=True
SECRET_KEY='622fa765fa110611a164164fa347e941687cb7711c4ad6f1017a448cdd4c8c64'
DEBUG=True
TESTING=True

if env == 'PRODUCTION':
  MONGODB_SETTINGS = {
    'DB': os.environ['MONGO_DB'],
    'host': os.environ['MONGOHQ_URL']
  }
else:
  MONGODB_SETTINGS = {
    'DB': 'webstub',
    'HOST': 'localhost'
  }
