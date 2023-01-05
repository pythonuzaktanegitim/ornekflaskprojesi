from flask import Flask
from . import config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'tahmin edemezsin'
app.config.from_object(config.Config)

from app import routes