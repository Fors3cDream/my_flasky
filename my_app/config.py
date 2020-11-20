from my_app import BASE_DIR

# Flask用这个秘钥保护用户会话，以防被篡改
# app.config['SECRET_KEY'] = 'hard to guess string' 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database/datas.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config:
    """Base config"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'sqlite:///' + os.path.join(BASE_DIR, 'database/datas.db')


class DevConfig(Config):
    DEBUG = True