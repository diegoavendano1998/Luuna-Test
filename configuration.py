class BaseConfig(object):
    'Base configuration'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*******@localhost:3306/luunatest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Tiempo de expiracion del token
    WTF_CSRF_TIME_LIMIT = 2000
    USER_ENABLE_EMAIL = True
    UPLOAD_FOLDER = r"/home/diego/Documents"
    USER_APP_NAME = "Luuna Test"
class ProductionConfig(BaseConfig):
    'Produccion configuration'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuration'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'Desarrollo key'
    # Servicio flask-mail
    MAIL_SUPPRESS_SEND = False
    MAIL_SERVER = "smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = '47d8e5888734e1' #fanipof786@brbqx.com
    MAIL_PASSWORD = 'abfc11af980f96'
    MAIL_DEFAULT_SENDER = ("FlaskApp","admin@FlaskApp.mx")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    USER_EMAIL_SENDER_EMAIL = "admin@FlaskApp.mx"
    CACHE_TYPE = "simple"
    DEBUG_TB_INTERCEPT_REDIRECTS = False