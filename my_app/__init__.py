from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
db = SQLAlchemy(app)

# Flask用这个秘钥保护用户会话，以防被篡改
app.config['SECRET_KEY'] = 'hard to guess string' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database/datas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 导入顺序 - 先初始化db 再进行导入即可成功
from my_app.catalog.views import app_blue
app.register_blueprint(app_blue)