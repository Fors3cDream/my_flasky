from my_app import BASE_DIR
import os

# Flask用这个秘钥保护用户会话，以防被篡改
# app.config['SECRET_KEY'] = 'hard to guess string' 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database/datas.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config:
    """Base config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "hard to guess string"
    

    # Mail config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT =  587 #465 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database/datas.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True

config = {
    'Dev': DevConfig,
}