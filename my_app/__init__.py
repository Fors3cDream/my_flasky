from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

from my_app.config import DevConfig
app.config.from_object(DevConfig)

# app = Flask(__name__)
db = SQLAlchemy(app)

# 导入顺序 - 先初始化db 再进行导入即可成功
from my_app.catalog.views import app_blue
app.register_blueprint(app_blue)