import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    SECRET_KEY=os.environ.get('SECRET_KEY')or '123'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}