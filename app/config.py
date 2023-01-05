import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') if os.environ.get('SECRET_KEY') else 'tahmin edemezsin'
    