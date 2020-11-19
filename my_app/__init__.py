from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Flask用这个秘钥保护用户会话，以防被篡改
app.config['SECRET_KEY'] = 'hard to guess string' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database/data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)