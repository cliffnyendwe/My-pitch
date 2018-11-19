# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
#     # SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_ONYX_URL")

#     UPLOADED_PHOTOS_DEST = 'app/static/photos'
#     MAIL_SERVER = 'smtp.gmail.com'

#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# # email configuration
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

#     # simple mde configurations
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True

# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_ORANGE_URL")
#     DEBUG = True
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch_test'

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig
# }

import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:0710755176cliff@localhost/pitch'
    SECRET_KEY=os.environ.get('SECRET_KEY') or '1234'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_TEAL_URL")
    pass   

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/minutepitch'
    DEBUG = True
class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/minutepitch'
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}